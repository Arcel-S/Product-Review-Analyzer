from pyramid.view import view_config
from pyramid.response import Response
from ..models import Review
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN', 'hf_xxxxxxxxxxxxxxxxxxxx')
GEMINI_KEY = os.getenv('GEMINI_KEY', 'AIzaSyxxxxxxxxxxxxxxxxxx')

genai.configure(api_key=GEMINI_KEY)

@view_config(route_name='analyze_review', renderer='json', request_method='POST')
def analyze_review(request):
    try:
        data = request.json_body
        text = data.get('review_text')
        
        # 1. Simple Sentiment Analysis (using text keywords - Indonesian & English)
        try:
            text_lower = text.lower()
            # Define sentiment keywords - ENHANCED with more Indonesian words
            positive_words = [
                # English
                'good', 'great', 'excellent', 'amazing', 'awesome', 'best', 'love', 'perfect', 'wonderful',
                'fantastic', 'brilliant', 'outstanding', 'superb', 'nice', 'cool', 'awesome',
                # Indonesian - Positive
                'baik', 'bagus', 'hebat', 'sempurna', 'luar biasa', 'berkualitas', 'mantap', 'keren',
                'cepat', 'lancar', 'responsif', 'smooth', 'nyaman', 'comfortable', 'tahan lama', 'awet',
                'hemat', 'efisien', 'tajam', 'jernih', 'detail', 'memuaskan', 'puas'
            ]
            
            negative_words = [
                # English
                'bad', 'terrible', 'horrible', 'awful', 'worst', 'hate', 'poor', 'useless', 'worse',
                'disappointing', 'sucks', 'crap', 'trash', 'junk', 'weak', 'slow', 'broken', 'lag',
                # Indonesian - Negative
                'jelek', 'buruk', 'kecewa', 'tidak bagus', 'mengecewakan', 'worthless', 'cepat habis',
                'boros', 'cepat panas', 'panas', 'macet', 'lambat', 'lag', 'freeze', 'error', 'rusak',
                'tidak tahan', 'tidak responsif', 'buram', 'gelap', 'tidak jelas', 'mengecewakan',
                'tidak recommended', 'jangan beli', 'sakit', 'nyeri', 'tidak nyaman', 'tidak lancar'
            ]
            
            positive_count = sum(1 for word in positive_words if word in text_lower)
            negative_count = sum(1 for word in negative_words if word in text_lower)
            
            if negative_count > positive_count:
                confidence = min(0.99, 0.6 + (negative_count * 0.12))
                top = {'label': 'NEGATIVE', 'score': confidence}
            elif positive_count > negative_count:
                confidence = min(0.99, 0.6 + (positive_count * 0.12))
                top = {'label': 'POSITIVE', 'score': confidence}
            else:
                top = {'label': 'NEUTRAL', 'score': 0.5}
        except Exception as sentiment_error:
            print(f"Sentiment Error: {sentiment_error}")
            top = {'label': 'NEUTRAL', 'score': 0.5}

        # 2. Gemini - Key Points Extraction
        key_points = ""
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            gemini_res = model.generate_content(
                f"Ekstrak 3-5 poin penting dari review produk ini. Gunakan bahasa Indonesia. Format: bullet points (-). Singkat dan jelas.\n\nReview: {text}"
            )
            key_points = gemini_res.text if gemini_res.text else "Review analysis complete"
        except Exception as gemini_error:
            # Fallback: Generate key points from review text
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            if len(sentences) >= 3:
                key_points = "- " + "\n- ".join(sentences[:3])
            else:
                key_points = "- " + "\n- ".join(sentences)
        
        # 3. Save DB
        new_review = Review(
            product_name=data.get('product_name'),
            review_text=text,
            sentiment=top['label'],
            confidence=top['score'],
            key_points=key_points
        )
        request.dbsession.add(new_review)
        return new_review.to_json()
    except Exception as e:
        request.response.status = 500
        return {"error": str(e)}

@view_config(route_name='get_reviews', renderer='json', request_method='GET')
def get_reviews(request):
    reviews = request.dbsession.query(Review).order_by(Review.id.desc()).all()
    return [r.to_json() for r in reviews]