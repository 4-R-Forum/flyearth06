bluetooth.onBluetoothConnected(function () {
    bluetooth.startAccelerometerService()
    bluetooth.startButtonService()
    bluetooth.startLEDService()
})
