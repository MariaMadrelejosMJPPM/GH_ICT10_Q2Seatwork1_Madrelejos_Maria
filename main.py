# student club member checker
from pyscript import display, document


def button(e):
    document.getElementById('result').innerHTML = '  '
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()
    name = f"{first_name} {last_name}"
    monarch_members = ['Vita De Guzman','Chalanie Lumbang', 'Keona Valdez', 'Isabelle Cabatu', 'Destiny Reyes']
    member_checker = name in monarch_members

    display_message = (f'Sorry {first_name} {last_name}, your name is not on the list.', f'Congratulations {first_name} {last_name}! You are now part of the Monarch!')

    display(display_message[member_checker], target='result')