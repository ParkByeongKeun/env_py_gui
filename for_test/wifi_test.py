import wifi
import subprocess
def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlan0', ssid)

    if cell:
        return cell

    return False


def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
    scheme.save()
    return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False

def wifi_Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        signal = abs(cell.signal)
        if signal <= 50:
            wifilist.append([cell.ssid, 'Good'])
        elif signal <= 65:
            wifilist.append([cell.ssid, 'Soso'])
        else:
            wifilist.append([cell.ssid, 'Bad'])
    
    '''
    cell.signal
                <= 50           -> Good connection strength
                50 < && < 65    -> SoSo connection strength
                65 <=           -> Bad  connection strength

    '''

    return wifilist

if __name__ == '__main__':
    # Search WiFi and return WiFi list
    # print Search()

    # # Connect WiFi with password & without password
    # print Connect('OpenWiFi')
    # print Connect('ClosedWiFi', 'password')

    # # Delete WiFi from auto connect list
    # print Delete('DeleteWiFi')
    print(Search())
    # print(wifi_Search())
    # Connect('sangsanglab', '0327107179')