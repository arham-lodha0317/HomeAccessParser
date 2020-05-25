import scrapy
import datetime
from datetime import date

class GradesSpider(scrapy.Spider):
    name = 'grades'
    allowed_domains = ['hac.friscoisd.org']
    start_urls = ['https://hac.friscoisd.org/HomeAccess/Account/LogOn/']

    data = {}

    def parse(self, response):

        loginInfo = {
            "SCKTY00328510CustomEnabled": "False",    
            "Database": "10",
            "VerificationOption": "UsernamePassword",
            "LogOnDetails.UserName": self.username,
            "tempUN": self.username,
            "tempPW": self.password,
            "LogOnDetails.Password": self.password,
            "login": ""
        }
        yield scrapy.FormRequest.from_response(response, callback=self.after_login, formdata=loginInfo)

    def after_login(self, response):

        current_year = date.today().year
        
        getMarkingPeriod = {
            "ctl00$plnMain$ddlReportCardRuns": "3-" + str(current_year),
            "__EVENTTARGET": "ctl00$plnMain$btnRefreshView", "__EVENTARGUMENT": "", "__VIEWSTATE": "Bw7TvcLovcG8BkYffCGVkuHs5lkoQBcptQvQiTYXws2jKi2dMMPiUC6u6tVCfyylArIp0tAN7StNAhKZb5qfT1wY0l+2oLqjlXH0QaddrQouPti1uWRhaia5lksx7sbQOdgngzGQP1ZO/nCu1FQJ/2CMD7wZ8zUqWvBeYkudD2PITozeH0CK1TBaXp66OfjeWN5K30E/2r8WKJx+QrynKAk+c/3lqV8tsWBccOtL0pKsnxn20QVsMpg+bRAgs3dFSNxN8ueCHN/+d13SgkbIorolZh/sKn7b1IIlK+uVJjdUn0kk9skHtVXvJ5OhSUEd5ER+rDbgRQnuGIPmaJ09KNDwe/GMBHM3M1QNOGSRNfgbvoPQTcn9gENjgS94VxoY+HIUtzJ+wpABpTXBzR975ZKUTqV7j72+Fd7/wVMEmZV1uMFRrmMb2yfISRsaJCW7/DFIDZ2GcB77tvXejZPF5nJbrKNlPsJCC1O6afHEJ8W94YOEXzC8l5tbGzB2GpIhXMfs06UAaqp/l1e/XZ35V4f/Hu4jtdrZQ8i4r8qPFOZ5dBoska6bj3GEZpqirOEPGuDvrWTR9NnAliEKySASLw3iswzfDCslCTV8j6y3vJXh6uByAgasEXgKbIxOCrn/3i5ZSYwOVG04zej/fvrLOXONdNg/AXxAkJXXoTKKsdFONp+HvEssook4TUs0KQRLQwgnSroABgWf+TPZrg4aSOgFTU/GnRfB82VcFMdhku6oZDqHhE2L5CCL0DezBhDYzd83MhXDIVsSmNpkHGe5iGvfqplG1R4h+OvziGSTVrPn5LC1Al32Jni01UTOU/OuF0xcJ7nKGCTnbg8md0LG6glSgiFSi0ftCDyc6uQ+JR3PgB8Z0PZf0ehZYdmQYgb1FEzj2KGl6IMFJ0h33CQfzlu54D/t8GliUZ7nNnokm275ygJFLYEcZvUe7Oh7eMz617jTikw1i/Tsp73HlOb4cxCLGvRcMlQ4Gt4kC2uyvzYbOhSTYIw0lXXwBZqebyYrdcDYQes0nZLuK3M8/9NfPxoJYj14ZXKc8OgxZ9eNniHjEWuGJdgOPlYO1XV7XooRy8JmszkDxlkGM5RiNHJi1V7d0h//asB0aLDofVBpWA4IkNWAIGvCaaKPky+ukV3M9P41sBFa2ujwsN9COXwvtzp3rb7efap3e2kZ2jmoId9QFdI+7wuaWEeREuV7x0Oua2s3ihk4ep9Zju7Yghqy3TC7gKBwJvv7w+r6AkCHKjXZhah+vTyR96Nc78poqah6PCmsqDnmeS/9eSQ6vboSfV5tfovXhl3sOEipFAd3xAJssLMgPuKdUKQwnrxe2ltXo7gFOuW864OUZjHEXMp3wUeg9umx8Uwx4fZyXVCc1T8jqtnMpruY9QQ/K8I1zt20fe/SjfmFGTQlNcLd5lDYpACoNcJZjTU4bFrLNNM2FgWG/H/Osp8jC6pC3Y9j8sSb1usLOTi1OzPAFaemdESl5rXaZZTUggTxHqDtPo1NPvusoAwgAeRdlLEDX8TytxW3x27aoXQieOe/SMAmeL3SvYLLBApmT0hT9KiH1PtNV2d/LW5SMExecSkGd4SY00wU7an0BGHzGP6F004NNvZ+uHO6tgQHKryPGKRaKLLw0+iAb/RqobWHiC6gV8MG2hFiQRjuDuLayfrUC9iNVv6p17P2vYHGMJuLmQRRU/yXnFRtxmjIs5nO0v3pMQgypFm+KXdYC9q0qL2S2C533eC5NzPYKcOCyLJalg6BfiL6zwE=", "__VIEWSTATEGENERATOR": "B0093F3C", "__EVENTVALIDATION": "4UNRMxTwAX6kDkSNOtTqfFue6mYRj0d+2ZIgistZOHwSujJIP4lzGIxGPCfqWlgrSgaBgK6EGvRH980ZvqaibJJK0BU690YWDnyZ7Lw+ZtPHk2uRTWo9Z6kCmINsH/VIFirQ3c5oKAg1Z/3yXc4y5UcaE8kAAcsg9W6U9SfinzgeZFD4Gxa8ogBUtDT3Bt7PjA2s1uX7IB7p4HEf+YVmFJ7EcuClj+k1GEPp9BJ/f90GeFN/5pedM/TwKKST8MNjzt8tfcxZCKUipetIjdy847jQpFhsh/IjQ8/jMEsW8KKyfDU1MTfvIhv3jFemtZloudyy5hxyaJsJYKy3TNPiXi9fm5Lj4XalP6BCFv88ulbvdRugUR0r1OvM0arzqq8Cgj8fm9jnDh62EckalGNqMilPwaCbLgIOblewMjoQ+TbDjPEQtlPB9nRq6Z4KqxT7740x9bSk6E5RqRFxCwXhvWm4JZw1Q/X0xiF22SvNZQhI3z25d3l1+zFnVb4jktjczcqnJEW8YPGBrSJxvxgPBxtwxvt62owtu7Ftnt2gB5ib7+JniFQlJUKiaWrt4voUshqQPIbPmtXWjyEp6s1/oPvs2lxwusNRac3p+TLIFvE4ik1TGYIlMFOd/8SmPUa7+SsucvXKL9lWTWFejdTFSRmbVdtQgAXV+pJPKHT11mvgPuC1NI9WGFE5WPzEJ7apNHJf2CJlMoPl2NkN9XGpqqHgOA0f6Cx3PBcd6sWIPl6GfnoKut2d1vBrU/BAwSL3xgu7iPiC4H/suaQbdkrlSbZMvUWmYxWBuIFR8MRsNpyfNN9JW9OojnnYeYu50WoTG0VckLNKCmWgj6xQgAKHfkcuRQDX7PbKBLVtc2v+R0NEsHtWdZKh0LuhSOcb6i4Hv9CLXEtx2huUWbyMn/9j3kmwR7n/i9Kvzu0f1P4p/heR8L8HYrXSNJnTyD87YzAayQWbae+IOsjEwRrGOqHMy6fDnXylJF4A5AvSuD4SYhImntxBQBWo+mEjlt1ewxkCP6Z8XfDGaLOCxp5cmXTZ8keTw1SG6duQkjQrKI4T2hGl1v6U6pRJ+E7DREQFDwqjOMDx50anb3uLvG1X4ZNEC5L0AWJOw/5i7zNMYZekbeF7E+uXIDDVGRacw7aBKRs0X3UrZ/OFk0ziQX6EuwzpcVCSHpwQh9r7OfpLKSMnAo7PyREvJbV44QoKB2Y9cNiDG+C7oXGWbABF7QnlpY0vnZfUDUKMKHSJ4veEB0CCuaQ7fEiOcOdd1cLPP+MXlQqd+D1WaXhorzCg/CWWUR6Lr3h99g24nwYwKBcqaadrhJ+gUF7kUfbCnZZdztdQUKhgF45ivTU+qy/zIJz5flgAvyUZCirGwIMicsjjXMqrqoDyDRSlbOV+umu+FQ3rWbsIw/Nc3/tGjqa80oDxDWgjme7vgoBc0/3MgpIXQm3dmkY5nNSumn05RZCFicRqNq0Z0lPdLlqetmcDUEFVh4Ewt6iZAXntzLhs2nQyAEQAv5kABvLVLJAcIO+zlU6a+htRC1jioAUgrihhfMlQrT5kv005ZpIJsQvtyjJLhc+lTQiLHlyRXMybIoEe7aBTFNHeq0Hj376xNe2gn7JobV5MOoaS3bSL50CgwzTD1C57vKE=",
            "ctl00$plnMain$hdnValidMHACLicense": "Y", "ctl00$plnMain$hdnIsVisibleClsWrk": "N", "ctl00$plnMain$hdnIsVisibleCrsAvg": "N", "ctl00$plnMain$hdnJsAlert": "Averages+cannot+be+displayed+when++Report+Card+Run+is+set+to+(All+Runs).", "ctl00$plnMain$hdnTitle": "Classwork", "ctl00$plnMain$hdnLastUpdated": "Last+Updated", "ctl00$plnMain$hdnDroppedCourse": "+This+course+was+dropped+as+of+", "ctl00$plnMain$hdnddlClasses": "(All+Classes)", "ctl00$plnMain$hdnddlCompetencies": "(All+Classes)", "ctl00$plnMain$hdnCompDateDue": "Date+Due", "ctl00$plnMain$hdnCompDateAssigned": "Date+Assigned", "ctl00$plnMain$hdnCompCourse": "Course", "ctl00$plnMain$hdnCompAssignment": "Assignment", "ctl00$plnMain$hdnCompAssignmentLabel": "Assignments+Not+Related+to+Any+Competency", "ctl00$plnMain$hdnCompNoAssignments": "No+assignments+found", "ctl00$plnMain$hdnCompNoClasswork": "Classwork+could+not+be+found+for+this+competency+for+the+selected+report+card+run.", "ctl00$plnMain$hdnCompScore": "Score", "ctl00$plnMain$hdnCompPoints": "Points", "ctl00$plnMain$hdnddlReportCardRuns1": "(All+Runs)", "ctl00$plnMain$hdnddlReportCardRuns2": "(All+Terms)", "ctl00$plnMain$hdnbtnShowAverage": "Show+All+Averages", "ctl00$plnMain$hdnShowAveragesToolTip": "Show+all+student's+averages", "ctl00$plnMain$hdnPrintClassworkToolTip": "Print+all+classwork", "ctl00$plnMain$hdnPrintClasswork": "Print+Classwork", "ctl00$plnMain$hdnCollapseToolTip": "Collapse+all+courses", "ctl00$plnMain$hdnCollapse": "Collapse+All", "ctl00$plnMain$hdnFullToolTip": "Switch+courses+to+Full+View", "ctl00$plnMain$hdnViewFull": "Full+View", "ctl00$plnMain$hdnQuickToolTip": "Switch+courses+to+Quick+View", "ctl00$plnMain$hdnViewQuick": "Quick+View", "ctl00$plnMain$hdnExpand": "Expand+All", "ctl00$plnMain$hdnExpandToolTip": "Expand+all+courses", "ctl00$plnMain$hdnChildCompetencyMessage": "This+competency+is+calculated+as+an+average+of+the+following+competencies", "ctl00$plnMain$hdnCompetencyScoreLabel": "Grade", "ctl00$plnMain$hdnAverageDetailsDialogTitle": "Average+Details", "ctl00$plnMain$hdnAssignmentCompetency": "Assignment+Competency", "ctl00$plnMain$hdnAssignmentCourse": "Assignment+Course", "ctl00$plnMain$hdnTooltipTitle": "Title", "ctl00$plnMain$hdnCategory": "Category", "ctl00$plnMain$hdnDueDate": "Due+Date", "ctl00$plnMain$hdnMaxPoints": "Max+Points", "ctl00$plnMain$hdnCanBeDropped": "Can+Be+Dropped", "ctl00$plnMain$hdnHasAttachments": "Has+Attachments", "ctl00$plnMain$hdnExtraCredit": "Extra+Credit", "ctl00$plnMain$hdnType": "Type", "ctl00$plnMain$hdnAssignmentDataInfo": "Information+could+not+be+found+for+the+assignment", "ctl00$plnMain$ddlClasses": "ALL", "ctl00$plnMain$ddlCompetencies": "ALL", "ctl00$plnMain$ddlOrderBy": "Class"
        }

        currentPeriod = scrapy.Request(url='https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx',
                             callback=self.grades                                     )
        yield currentPeriod                     

    def grades(self, response):
        data = {}
        data['classes'] = []

        markingPeriod = response.xpath(
            '//span[@class="combobox_plnMain_ddlReportCardRuns"]').extract()
        print(markingPeriod)
        print('hello')

        AllAssignmentClasses = response.css("div.AssignmentClass")

        for assigmmentClass in AllAssignmentClasses:
            className = assigmmentClass.css(
                "a.sg-header-heading::text").extract()[0].strip()
            lastUpdated = assigmmentClass.css(
                "span.sg-header-sub-heading::text").extract()[0].strip()[15:-1]
            average = assigmmentClass.css(
                "a.sg-header-heading::text").extract()[0].strip()[15:]

            if len(lastUpdated) != 8:
                lastUpdated = str(0) + lastUpdated

            formatStr = '%m/%d/%Y'
            date = datetime.datetime.strptime(lastUpdated, formatStr)

            assignments = assigmmentClass.css('tr.sg-asp-table-data-row')

            assignmentList = []

            for i in assignments:
                assignmentName = i.css('a::text').extract()
                if len(assignmentName) != 0:
                    name = assignmentName[0].strip()
                    typeOfGrade = i.css('td::text')[5].extract().strip()
                    number = i.css('td::text')[11].extract().strip()

                    assignmentInfo = {
                        "Name": name,
                        "Type": typeOfGrade,
                        "Grade": number
                    }

                    assignmentList.append(assignmentInfo)

            classData = {
                'className': className,
                'lastUpdated': {
                    'months' : date.month,
                    'days': date.day,
                    'years':date.year,
                },
                'average': average,
                'Assignments': assignmentList
            }

            data['classes'].append(classData)
            

        yield data
