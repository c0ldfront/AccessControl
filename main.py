from AccessController import StationeersLoader, ArkLoader, EcoLoader, SELoader, ValheimLoader


def StationeersExample():
    file_path = 'C:\\Users\\coldf\\PycharmProjects\\pythonProject\\examples\\'
    file_name = 'SNWhitelist.txt'
    try:
        with StationeersLoader(file_path, file_name) as station_data:
            station_data.add('newUser')
            station_data.add('removeMe')
            # station_data.remove('removeMe')
            # print(station_data.find_one('removeMe'))
            # print(station_data.find_all())
            # station_data.clear()
    except Exception as e:
        print(e)


def ArkExample():
    file_path = 'C:\\Users\\coldf\\PycharmProjects\\pythonProject\\examples\\'
    file_name = ' '
    try:
        with ArkLoader(file_path, file_name) as ark_data:
            ark_data.add('newUser')
            ark_data.add('removeMe')
            # ark_data.remove('removeMe')
            # print(ark_data.find_one('removeMe'))
            # print(ark_data.find_all())
            # ark_data.clear()
    except Exception as e:
        print(e)


def EcoExample():
    file_path = 'C:\\Users\\coldf\\PycharmProjects\\pythonProject\\examples\\'
    file_name = 'Users_example.eco'
    try:
        with EcoLoader(file_path, file_name) as eco_data:
            eco_data.add(['newUser', 'newUser2', 'newUser3', 'newUser4', 'newUser5'])
            # eco_data.add('newUser')
            # eco_data.add('removeMe')
            # eco_data.remove('removeMe')
            # print(eco_data.find_one('removeMe'))
            # print(eco_data.find_all())
            # eco_data.clear()
    except Exception as e:
        print(e)


def SpaceEngineersExample():
    file_path = 'C:\\Users\\coldf\\PycharmProjects\\pythonProject\\examples\\'
    file_name = 'se_example.xml'
    try:
        with SELoader(file_path, file_name) as se_data:
            se_data.add('newUser')
            # se_data.add('removeMe')
            # se_data.clear()
            # se_data.add(['newUser', 'newUser2', 'newUser3'])
            # se_data.remove('removeMe')
            # print(se_data.find_one('removeMe'))
            # print(se_data.find_all())
            # se_data.clear()
    except Exception as e:
        print(e)


def ValheimExample():
    file_path = 'C:\\Users\\coldf\\PycharmProjects\\pythonProject\\examples\\'
    file_name = 'permittedlist.txt'
    try:
        with ValheimLoader(file_path, file_name) as val_data:
            val_data.add('newUser')
            val_data.add('removeMe')
            # val_data.remove('removeMe')
            # print(val_data.find_one('removeMe'))
            # print(val_data.find_all())
            # val_data.clear()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # StationeersExample()
    # ArkExample()
    # EcoExample()
    SpaceEngineersExample()
    # ValheimExample()
