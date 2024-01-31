
from utilities.readProperties import Readconfig
from PageObject.FlightBookingPage import flight_booking_page
from utilities.customLogger import LogGen

class Test_001_FlightSearch:
    baseurl=Readconfig.appApplicationUrl()
    fromDestination=Readconfig.getFromDestinatin()
    toDestination=Readconfig.getToDestination()
    logger=LogGen.loggen()

    def test_SearchFlight(self,setup):
        self.logger.info("*********** Test_001_Login ********** ")
        self.logger.info("*********** Verifying search flight ********** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.fp=flight_booking_page(self.driver)
        self.fp.clickLoginCloseWindow()
        self.fp.clickFlightsOption()
        self.fp.setFromDestination(self.fromDestination)
        self.fp.setToDestination(self.toDestination)
        self.fp.setDepartureDate()
        self.fp.clickButtonDone()
        self.fp.buttonSearchFlights()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchFlight.png")
        self.logger.info("*********** Search flight completed ********** ")

