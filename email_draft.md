Dear manager, 

We have found the following highlights for the data
- There is some suspicious activity of web scrapers and unidentified users
- The most accessed lesson was Javascript I and the least accessed is K means testing
- Grads continue to access Javascript I and MySQL lessons
- There is evidence of cross curriculum traffic

Below are more detailed answers to your questions, in addition to the attached google slide and final notebook called Report.  Please let us know if there are any other questions you have.

Thanks, 
Cayt S., David M., Eriberto C. and Stephen F.
Data Science Team

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
- The lesson 'javascript-i' appears to be the most frequently trafficked site across all programs in the Codeup curriculum log database
- Following the most visited, the lessons known as 'TOC' and 'search/search_index.json' are the two runner-ups for most frequently trafficked sites.
- Based off analysis of the domain, it is my theory that .json maybe indicative of web-scraping activity. If I have sufficient time, this theory will be explored further.

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
The Classification module in the curriculum was accessed significantly more by Darden compared to the other cohorts

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?

A : The student in the who were in the bottom 25% of number of pings had an average of accessing the curriculum 102 days before the end of thier cohort, and 75% had their last access date 22 days before the end of the cohort.  Therefore it seems likely that the students had left the program without graduating.

4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

A:  There is evidence of webscraping.  For example, ip `216.1.153.162` moves through a lot of pages within seconds.  There are a series of user_id that are not associated with any cohort; these could be suspicious-- particularly since some of them seem to be on the wifi.  It could be the case that they could be guests using the network, but there are more nefarious interpretations of this.

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

A: Given the timelines mentioned, I was unable to concretely define certain curriculums by program.  This is likely mostly due to treating each program seperately instead of aggregating by full_stack_php, full_stack_java and front_end.  Treating 2020+ data as 'clean', I was able to identify times at which programs had cross-curriculum activity. However, the timelines in the plot do not seem to match with this question, as most of 2019 contained cross-curriculum activity.  Looking into it a little more, it seems that all the registered activity is between full_stack_php and full_stack_java.

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

A:
- Full stack java and php cohorts accessed these classes most after graduation:
  - Javascript i
  - Html - css
  - spring
- Data Science cohorts accessed these classes most after graduation:
  - Intro to Data Science
    - Note: this was aggregated across multiple naming conventions - likely due to a change in website structure
  - MySQL Overview
  - Classification Overview

7. Which lessons are least accessed?
- Pandas overview
- objects
- navigating the file system
- clasification acquiredata
- file paths darden python assement
- inspect
- bom and dom
- project planning and explore 
- open data
- excel shortcuts
- kmeans2