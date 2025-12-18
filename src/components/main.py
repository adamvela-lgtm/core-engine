import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def main():
    if len(sys.argv) != 2:
        logging.error('Usage: python main.py <config_file>')
        sys.exit(1)

    config_file = sys.argv[1]
    if not os.path.exists(config_file):
        logging.error('Config file not found')
        sys.exit(1)

    with open(config_file, 'r') as f:
        config = {}
        for line in f:
            key, value = line.strip().split('=')
            config[key] = value

    # Validate config
    required_keys = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
    for key in required_keys:
        if key not in config:
            logging.error(f'Missing required config key: {key}')
            sys.exit(1)

    try:
        db_host = config['DB_HOST']
        db_user = config['DB_USER']
        db_password = config['DB_PASSWORD']
        db_name = config['DB_NAME']

        # Connect to database
        import sqlite3
        conn = sqlite3.connect(f'sqlite:///{db_name}?host={db_host}&user={db_user}&password={db_password}')

        # Run queries
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')
        results = cursor.fetchall()

        # Print results
        for result in results:
            print(result)

    except sqlite3.Error as e:
        logging.error(f'Database error: {e}')

if __name__ == '__main__':
    main()