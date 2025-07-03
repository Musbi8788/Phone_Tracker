import gps

def get_gps_data():
    session = gps.gps(mode=gps.WATCH_ENABLE)  # Watch mode to continuously fetch data
    while True:
        report = session.next()  # Get the next GPS report
        if report['class'] == 'TPV':  # TPV (Time-Position-Velocity) report contains location data
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                print(f"Latitude: {report.lat}, Longitude: {report.lon}")
                break  # Remove this break to keep the loop running for continuous tracking

get_gps_data()
