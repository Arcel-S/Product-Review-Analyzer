import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models

def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.
    """
    # Kita buat 1 contoh review dummy agar database tidak kosong
    model = models.Review(
        product_name='Contoh Produk Awal', 
        review_text='Ini adalah data contoh inisialisasi.',
        sentiment='NEUTRAL',
        confidence=0.5,
        key_points='- Data awal\n- Testing'
    )
    dbsession.add(model)

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize the database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server process is running.

3.  Your SQL database connection settings might be out of date.
    Check your .ini file for a [app:main] section with the
    sqlalchemy.url setting.
''')
        sys.exit(1)

if __name__ == '__main__':
    main()