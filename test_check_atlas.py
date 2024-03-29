from pages.campaign_design_page import CampaignDesignPage
from pages.campaign_details_page import CampaignDetailsPage
from pages.campaign_generate_page import CampaignGeneratePage
from pages.campaign_launch_page import CampaignLaunchPage
from pages.campaign_rule_page import CampaignRulePage
from pages.campaign_start_page import CampaignStartPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class MyStepsTest(BaseTest):
    email = "idil.sen@useinsider.com"
    password = "*************************"

    def test_steps(self):
        login_page = LoginPage(self.driver)
        login_page.fill_login_form(self.email, self.password)
        login_page.click_login_btn()

        campaign_start_page = CampaignStartPage(self.driver)
        campaign_start_page.select_instory()
        campaign_start_page.create_campaign()

        campaign_rule_page = CampaignRulePage(self.driver)
        campaign_rule_page.campaign_rule_step()

        campaign_design_page = CampaignDesignPage(self.driver)
        camp_id = campaign_design_page.campaign_design_step()

        campaign_launch_page = CampaignLaunchPage(self.driver)
        campaign_launch_page.campaign_launch_step()

        campaign_generate_page = CampaignGeneratePage(self.driver)
        campaign_generate_page.campaign_generate_step()

        campaign_details_page = CampaignDetailsPage(self.driver)
        campaign_details_page.campaign_details_step()
        campaign_details_page.campaign_open_test_link_step()
