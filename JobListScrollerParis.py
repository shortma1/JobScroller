import csv
import datetime
# Initialize flag
flag = 0
x = datetime.datetime.now()
# Set output file name
output = open("C:\\Users\\short\\PycharmProjects\\ScrollerParser\\Level1JobScrollParis.htm", 'w')
# HTML Header Start
output.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n')
output.write('"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
output.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
output.write('<head>\n')
output.write('<meta http-equiv="refresh" content="1800" />\n')
output.write('<title>Workforce Solutions North East Texas</title>\n')
output.write('<style type="text/css" media="screen">\n')
output.write('#first {\n')
output.write('height:30px;\n')
output.write('background-color:yellow;\n')
output.write('text-align:center;\n')
output.write('margin: -18px -10px 10px 10px;\n')
output.write('padding: 0px 0px 0px 0px;\n')
output.write('border-bottom: #bbbbbb 1px dashed;\n')
output.write('}\n')
output.write('h1 {\n')
output.write('margin: 0px -10px 0px -10px;\n')
output.write('padding: 10px 10px 5px 10px;\n')
output.write('font: 900 2em/1.1em Verdana; Arial, sans-seriff;\n')
output.write('color: white;\n')
output.write('height: 120px;\n')
output.write('background-color: #7d7d7d;\n')
output.write('}\n')
output.write('img {\n')
output.write('float: left;\n')
output.write('margin: 0px 0px 0px 0px;\n')
output.write('padding: 0px 15px 0px 0px;\n')
output.write('}\n')
output.write('h2 {\n')
output.write('margin: -27px -10px 0px -10px;\n')
output.write('padding: 0px 5px 5px 15px;\n')
output.write('font: 800 1.5em/1.0em Verdana; Arial, sans-seriff;\n')
output.write('color: white;\n')
output.write('background-color: #7d7d7d;\n')
output.write('}\n')
output.write('table {\n')
output.write('padding:0px;\n')
output.write('border-spacing:0px;\n')
output.write('width:100%;\n')
output.write('}\n')
output.write('tr {\n')
output.write('height:50px;\n')
output.write('padding:0px;\n')
output.write('border-spacing:0px;\n')
output.write('}\n')
output.write('</style>\n')
output.write('</head>\n')
output.write('<body>\n')
output.write('<h1>\n')
output.write('<img src="Picture2.png" />\n')
output.write('<center>\n')
output.write('<i>Daily Paris Job Postings for ')
output.write(x.strftime("%A"))  # Outputs Day of Week
output.write(" ")
output.write(x.strftime("%B"))  # Outputs Month
output.write(" ")
output.write(x.strftime("%d"))  # Outputs number day of month
output.write(",")
output.write(" ")
output.write(x.strftime("%Y"))  # Outputs Year
output.write('<br />\n')
output.write('--Current Open Job Listings--<br /></center>\n')
output.write('</i></h1>\n')
output.write('<div id="first">\n')
output.write('<h3>\n')
output.write('Please write down any job posting ID numbers that interests you and look them up on the Work In Texas website.\n')
output.write('</h3>\n')
output.write('</div>\n')
output.write('<div\n')
output.write('align="left"><marquee bgcolor="#ffffff" scrollamount="2"\n')
output.write('direction="up" loop="true" width="1900" height="797">\n')
output.write('<font color="#000000" size="7">\n')
output.write('<table cellspacing="0" cellpadding="0"">\n')
output.write('<tr><td width="1200"> </td><td width="1800"> </td><td width="1900"> </td></tr><tr><td> </td><td> </td><td> </td><tr><tr><td> </td><td> </td><td> </td><tr>\n')
# HTML Header End

with open('C:\\Users\\short\\PycharmProjects\\ScrollerParser\\DailyPostingParis.csv', "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if flag == 0:
            output.write('<tr bgcolor="#CCCCCC"><td>')
        else:
            output.write('<tr><td>')
        # Job ID
        output.write(row['JobOrderID'])
        output.write('</td><td>')
        # Job Title
        output.write(row['JobTitle'])
        output.write('</td><td>')
        # Job City
        output.write(row['JobCity'])
        output.write('</td></tr>')
        output.write('\n')
        if flag == 0:
            output.write('<tr bgcolor="#CCCCCC"><td>')
        else:
            output.write('<tr><td>')
        # Full Part Time
        if (row['FullPartTime']) == 'Full Time (30 Hours or More)':
            output.write('Full Time')
        else:
            output.write('Part Time')
        output.write('</td><td>')
        # Experience Required
        if (row['MonthsExp']) < '1':
            output.write('No Experience Required')
        else:
            output.write(row['MonthsExp'])
            output.write('Months Experience Required')
        output.write('</td><td>')
        # Drivers License
        if (row['DriversLicenseReq']) == 'No':
            output.write('No Driver\'s License Required')
        elif (row['DriversLicenseReq']) == 'Yes, Operator License':
            output.write('Driver\'s License Required')
        elif (row['DriversLicenseReq']) == 'Yes, Commercial License':
            output.write('Commercial DL Required')
        else:
            output.write(row['DriversLicenseReq'])
        output.write('</td></tr>')
        output.write('\n')
        if flag == 0:
            output.write('<tr bgcolor="#CCCCCC"><td>')
        else:
            output.write('<tr><td>')
        # Wage
        if len(row['Wage']) == 0:
            output.write('Pay not listed')
        elif (row['Wage']) == "0.00":
            output.write('Pay not listed')
        else:
            output.write('$')
            output.write(row['Wage'])
            output.write(' / ')
            output.write(row['SalaryUnit'])
        output.write('</td><td>')
        # Hours
        if len(row['Hours']) == 0:
            output.write('No working Hours listed')
        else:
            output.write(row['Hours'])
            output.write(' Hours Weekly')
        output.write('</td><td>')
        # Education Level
        if len(row['EduLvl']) == 0:
            output.write('No Minimum Education Required')
        elif (row['EduLvl']) == 'High School Diploma or Equivalent':
            output.write('HS Diploma/GED Required')
        else:
            output.write(row['EduLvl'])
            output.write(' Required')
        output.write('</td></tr>')
        output.write('\r\n')
        # Reset the flag for the next round
        if flag == 0:
            flag = 1
        else:
            flag = 0
output.write('</table>')
output.write('</body>')
output.write('</html>')
output.close()
