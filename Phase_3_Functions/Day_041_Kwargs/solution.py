# Day 41 Solutions

# Challenge 1
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

display_info(name='Alice', age=30, city='Cape Town')
print()
display_info(title='Python Crash Course', author='Matthes', year=2019, pages=544)

# Challenge 2
def create_profile(username, **details):
    print(f'Profile: {username}')
    if details:
        for key, val in details.items():
            print(f'  {key}: {val}')
    else:
        print('  (no details provided)')

create_profile('alice99')
print()
create_profile('bob42', email='bob@mail.com', age=25, city='Durban')

# Challenge 3
def configure(host='localhost', port=8080, **options):
    print(f'host: {host}')
    print(f'port: {port}')
    if options:
        print('Additional options:')
        for key, val in options.items():
            print(f'  {key}: {val}')

configure()
print()
configure(host='prod.server')
print()
configure('staging', 3000, debug=True, log_level='info', max_connections=100)

# Challenge 4
def book_flight(destination, passengers, class_type='economy'):
    print(f'Booking {passengers} seat(s) to {destination} ({class_type})')

booking1 = {'destination': 'Paris', 'passengers': 2}
booking2 = {'destination': 'Tokyo', 'passengers': 1, 'class_type': 'business'}

book_flight(**booking1)
book_flight(**booking2)

defaults = {'destination': 'London', 'passengers': 1, 'class_type': 'economy'}
overrides = {'passengers': 3, 'class_type': 'business'}
book_flight(**{**defaults, **overrides})

# Challenge 5
def build_report(title, *sections, **metadata):
    print(f'=== {title} ===')
    for i, section in enumerate(sections, 1):
        print(f'{i}. {section}')
    if metadata:
        print('--- Metadata ---')
        for key, val in metadata.items():
            print(f'{key}: {val}')

build_report(
    'Monthly Sales Report',
    'Revenue increased by 12%.',
    'Top product: Widget Pro.',
    'Customer complaints down 5%.',
    author='Alice',
    date='2024-11-01',
    version='2'
)
