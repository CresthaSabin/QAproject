class Locate:
    """Stores all locators used in the framework."""

    # Login Page Locators
    nav_signin_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    email_field_id = "email"
    password_field_id = "passwd"
    login_btn_xpath = '//*[@id="SubmitLogin"]/span'

    # Add to Cart
    yourLoga_Logo_id = "header_logo"
    image1_xpath='//*[@id="blocknewproducts"]/li[1]/div/div[2]/h5/a'
    addtocart1_xpath='//*[@id="add_to_cart"]/button/span'
    contshopping_xpath='//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
    popular_xpath= '//*[@id="home-page-tabs"]/li[2]/a'

    image2_xpath= '//*[@id="homefeatured"]/li[2]/div/div[2]/h5/a'
    addtocart_xpath='//*[@id="add_to_cart"]/button/span'

    # Checkout
    checkout_button1_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'
    checkout_button2_xpath = '//*[@id="center_column"]/p[2]/a[1]/span'
    checkout_button3_xpath = '//*[@id="center_column"]/form/p/button/span'
    check_box_xpath = '//*[@id="cgv"]'

    checkout_button4_xpath = '//*[@id="form"]/p/button/span'
    pay_by_bank_xpath = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a/span'
    confirm_my_order_xpath = '//*[@id="cart_navigation"]/button/span'


    #Show Order
    show_order_Xpath = '//*[@id="center_column"]/div/div[1]/ul/li[1]/a/span'









