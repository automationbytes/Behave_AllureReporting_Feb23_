from behave import __main__ as runner
import sys
import os

if __name__ == '__main__':
    sys.stdout.flush()

    FeatureFilePath = "FeaturesFiles"
    Tags = " --tags=Regression,Sanity"
    AllureReportPath = " -f allure_behave.formatter:AllureFormatter -o Reports"
    BehaveOptions = ' -f html-pretty -o behave-report.html --color --summary --verbose'
    run = FeatureFilePath+Tags+AllureReportPath+BehaveOptions
    runner.main(run)

    reportdir = os.getcwd()+"/Reports"
    os.system('cmd /c "allure serve "'+reportdir)


    ''''
    Tags = " --tags=Regression" #only regression
    Tags = " --tags= -Regression" #exclude regression    
    Tags = " --tags=Regression,Sanity   #0r
    Tags = " --tags=Regression --tags=Sanity #and
    
    '''