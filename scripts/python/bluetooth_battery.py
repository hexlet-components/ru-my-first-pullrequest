from bluetooth_battery import BatteryStateQuerier, BatteryQueryError, BluetoothError

query = BatteryStateQuerier("6C:CE:44:33:8A:BF")
print(query)
