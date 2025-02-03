class Locate:
    """Stores all locators used in the framework."""

    # Login Page Locators
    nav_signin_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    email_field_id = "email"
    password_field_id = "passwd"
    login_btn_xpath = '//*[@id="SubmitLogin"]/span'

    # Home Page
    homepage_logo_xpath = '//*[@id="header_logo"]/a/img'

    # Add to Cart Locators
    product1_xpath = '//*[@id="blocknewproducts"]/li[1]/div/div[1]/div/a[1]/img'
    addtocart_xpath = '//*[@id="blocknewproducts"]/li[1]/div/div[2]/div[2]/a[1]/span'
