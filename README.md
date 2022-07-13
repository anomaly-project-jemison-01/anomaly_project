Anomaly detection project repo

`env_example.py` is how the `env.py` module should be written to work properly with `wrangle.py`

# Email sent to datascience@codeup.com

Hello,

Here are a few highlights on the web server traffic:

- There is some suspicious activity of web scrapers and unidentified users
- The most accessed lesson was Javascript I and the least accessed lesson was K means testing
- Alumni primarily access the Javascript I and MySQL lessons post-graduation.
- There is evidence of cross-curriculum traffic

You can find a slide for your presentation here.  Some of the code and support graphs can be found in our report - located here on github.

More detailed responses to each question can be found below.  Let us know if you have any questions.

Best,

Cayt S., David M., Eriberto C., Stephen F
Codeup | Jemison Cohort

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

- The lesson 'javascript-i' appears to be the most frequently trafficked site across all programs in the Codeup curriculum log database
- Following the most visited, the lessons known as 'TOC' and 'search/search_index.json' are the two runner-ups for most frequently trafficked sites.
- Based on analysis of the domain, it is my theory that .json may be indicative of web-scraping activity. If I have sufficient time, this theory will be explored further.

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?

    The Classification module in the curriculum was accessed significantly more by Darden compared to the other cohorts

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?

The students who were in the bottom 25% of number of pings had an average of accessing the curriculum 102 days before the end of their cohort, and 75% had their last access date 22 days before the end of the cohort.  Therefore it seems likely that the students had left the program without graduating.

4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

There is evidence of web scraping.  For example, ip `216.1.153.162` moves through a lot of pages within seconds.  There are a series of user_id that are not associated with any cohort; these could be suspicious-- particularly since some of them seem to be on the wifi.  It could be the case that they could be guests using the network, but there are more nefarious interpretations of this.

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

Given the timelines mentioned, I was unable to concretely define certain curriculums by program.  This is likely mostly due to treating each program 

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

Given the timelines mentioned, I was unable to concretely define certain curriculums by program.  This is likely mostly due to treating each program separately instead of aggregating by full_stack_php, full_stack_java and front_end.  Treating 2020+ data as 'clean', I was able to identify times at which programs had cross-curriculum activity. However, the timelines in the plot do not seem to match with this question, as most of 2019 contained cross-curriculum activity.  Looking into it a little more, it seems that all the registered activity is between full_stack_php and full_stack_java.

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

Full stack java and php cohorts accessed these classes most after graduation:
    - Javascript i
    - Html - css
    - spring
Data Science cohorts accessed these classes most after graduation:
    - Intro to Data Science
        - Note: this was aggregated across multiple naming conventions - likely due to a change in website structure
    - MySQL Overview
    - Classification Overview

7. Which lessons are least accessed?

- Pandas overview
- objects
- navigating the file system
- classification acquiredata
- file paths darden python assessment
- inspect
- bom and dom
- project planning and explore
- open data
- excel shortcuts
- kmeans2