import allure


def after_step(context,step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_file(), name=step.name,
                      attachment_type=allure.attachment_type.PNG)
