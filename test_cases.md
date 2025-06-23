### General Website Behavior

| Test Case ID | Test Case Description                        | Steps to Execute                              | Expected Result                                  |
|--------------|---------------------------------------------|----------------------------------------------|-------------------------------------------------|
| GN-001       | Verify language selector is accessible       | Navigate to homepage, check header/footer for language selector | Language selector is visible and accessible      |
| GN-002       | Verify changing language updates all content| Select a different language (e.g., Spanish)  | All page text updates to selected language       |
| GN-003       | Verify language preference retained on navigation | Change language, navigate to different pages | Language remains changed on all pages             |
| GN-007       | Verify page title appears in browser tab     | Open any website page                         | Browser tab shows correct page title              |
| GN-004       | Verify homepage sections are clearly visible | Load homepage                                | All major homepage sections (Hero, Features, Footer, etc.) are visible |
| GN-005       | Verify all sections load without errors       | Scroll through homepage                       | All sections load with correct content and no errors |

---

### Header Section Test Cases (Header)

| Test Case ID | Test Case Description                             | Steps to Execute                                              | Expected Result                                               |
|--------------|--------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Header_01    | Verify the OrangeHRM logo is displayed and clicking it redirects to the homepage. | 1. Locate the logo in the header. 2. Click on the logo.       | The OrangeHRM logo is visible and clicking it reloads/redirects to the homepage (https://www.orangehrm.com/). |
| Header_02    | Verify that the header section is displayed on the homepage. | Open the URL: https://www.orangehrm.com/ Observe the top section of the page. | The header section is visible at the top of the page.         |
| Header_03    | Verify all main navigation menu items are present and clickable. | 1. Inspect the navigation menu in the header. 2. Verify menu items like "Products," "Solutions," "Resources," "Pricing," "Contact," "Login," etc. 3. Click each menu item and verify it redirects or opens dropdown. | All menu items are displayed correctly, clickable, and navigate to the correct pages or show dropdown menus. |
| Header_04    | Verify dropdown menus appear on hover/click on navigation items that have submenus. | 1. Hover over or click the menu items like "Products," "Solutions," or "Resources" that have dropdowns. | The dropdown menu appears with relevant submenu items, and each submenu item is clickable and redirects properly. |
| Header_05    | Verify the header layout adjusts correctly on desktop, tablet, and mobile screen sizes. | 1. Open the website on desktop browser. 2. Resize window to tablet and mobile sizes or use device simulation. 3. Observe header element arrangement. | The header adapts responsively, with menus collapsing into a hamburger icon on smaller screens, maintaining usability. |
| Header_06    | Verify the hamburger menu icon appears on mobile view and clicking it expands/collapses the menu. | 1. Switch to mobile screen view. 2. Locate and click the hamburger menu icon in the header. 3. Observe the expanded menu options. | The hamburger icon is visible, and clicking it toggles the display of the navigation menu items. |
| Header_07    |                                                  |                                                              |                                                              |
| Header_08    | Verify the header is accessible via keyboard navigation (Tab key) and screen readers. | 1. Use the Tab key to navigate through all header elements. 2. Ensure focus states are visible. 3. Use a screen reader to verify meaningful labels. | All header elements are accessible via keyboard and screen readers, with proper focus indicators and labels. |
| Header_09    | Verify the header and its elements load promptly when the page loads. | 1. Open the website and measure the time taken for the header to appear. | The header and its components load quickly without delay or broken images. |

---

### Book a Free Demo Button Test Cases (DemoBtn)

| Test Case ID  | Test Case Description                                        | Steps to Execute                                         | Expected Result                                             |
|---------------|-------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------|
| DemoBtn_01    | Verify the "Book a Free Demo" button is visible on the page  | 1. Open the page containing the button (e.g., homepage). 2. Locate the "Book a Free Demo" button. | Button is visible, enabled, and clearly labeled.            |
| DemoBtn_02    | Verify clicking "Book a Free Demo" navigates to the demo booking page | 1. Click the Book a Free Demo button.                    | Browser navigates to https://www.orangehrm.com/en/book-a-free-demo |
| DemoBtn_03    | Verify URL after clicking Book a Demo button is correct       | 1. Click the Book a Demo button.                         | Address bar shows exact URL https://www.orangehrm.com/en/book-a-free-demo |
| DemoBtn_04    | Verify Book a Free Demo page loads without errors             | 1. Navigate to https://www.orangehrm.com/en/book-a-free-demo | Page loads fully with no broken images/scripts.              |
| DemoBtn_05    | Verify page title and heading reflect "Book a Free Demo"      | 1. Check browser tab title and page main header.         | Title and header clearly state "Book a Free Demo".           |
| DemoBtn_06    | Verify demo booking form is present on the page               | 1. Locate form fields for name, email, company, phone, etc. | Form fields for required information are visible.            |
| DemoBtn_07    | Verify required fields (e.g., Name, Email) are marked and validation occurs if left empty. | 1. Try submitting form leaving required fields blank.   | Appropriate error messages shown, submission blocked.        |
| DemoBtn_08    | Verify email field validates email format                      | 1. Enter invalid emails ("abc@", "123", "test.com"). 2. Submit form. | Validation error prevents submission and prompts valid email. |
| DemoBtn_09    | Verify that submitting the form with valid inputs completes successfully and shows a confirmation message. | Fill all required fields with valid data. Click the submit/book demo button. | Form submits successfully with confirmation message or page. |
| DemoBtn_11    | Verify captcha works properly                                  | 1. Attempt submission without completing captcha         | Submission blocked with error prompting captcha completion. |
| DemoBtn_12    | Verify that text fields accept only text, phone number fields accept numbers, email fields accept emails, etc. | 1. Enter invalid data types (e.g., letters in phone number). | Validation prevents incorrect input or shows error messages. |
| DemoBtn_13    | Verify page responsiveness on various devices                 | 1. Open page on desktop, tablet, and mobile or simulate screen sizes. | Layout adjusts correctly with no broken elements.            |
| DemoBtn_14    | Verify privacy policy or terms & conditions link              | 1. Locate and click privacy/terms link near the form.    | Link opens the relevant document/page in a new tab or window. |
| DemoBtn_15    | Verify the page and form are accessible (keyboard navigation, alt text on images, proper labels). | 1. Navigate form using keyboard only. 2. Check screen reader labels and alt text. | Form fully accessible and usable without mouse.              |

---

### Contact Sales Button Test Cases (ContactSalesBtn)

| Test Case ID      | Test Case Description                                  | Steps to Execute                                      | Expected Result                                                  |
|-------------------|-------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------|
| ContactSalesBtn_01 | Verify the "Contact Sales" button is visible          | 1. Open the page with the Contact Sales button (e.g., homepage). 2. Locate the "Contact Sales" button. | Button is visible, enabled, and labeled correctly.              |
| ContactSalesBtn_02 | Verify clicking "Contact Sales" navigates page        | 1. Click the "Contact Sales" button.                  | Browser navigates to https://www.orangehrm.com/en/contact-sales |
| ContactSalesBtn_03 | Verify 'Contact Sales' navigates to contact form       | Click 'Contact Sales' link                             | Contact form/page opens                                          |
| ContactSalesBtn_04 | Verify that the URL after clicking the button is exactly https://www.orangehrm.com/en/contact-sales. | 1. Click the Contact Sales button.                    | Address bar URL matches exactly https://www.orangehrm.com/en/contact-sales |
| ContactSalesBtn_05 | Verify Contact Sales page loads successfully            | Navigate directly to https://www.orangehrm.com/en/contact-sales or via the Contact Sales button. | Page loads fully with no broken images, errors, or missing elements. |
| ContactSalesBtn_06 | Verify page title and main heading                      | 1. Check browser tab title. 2. Check main page header. | Both display "Contact Sales" clearly.                           |
| ContactSalesBtn_07 | Verify presence of Contact Sales form                   | 1. Locate the contact form on the page.                | Form with expected fields (name, email, company, phone, message, etc.) is visible. |
| ContactSalesBtn_08 | Verify required fields and validation                    | 1. Attempt to submit form without filling required fields. | Form submission blocked; error messages appear for each missing required field. |
| ContactSalesBtn_09 | Verify email field validates email format               | 1. Enter invalid emails (e.g., "abc", "abc@", "123"). 2. Attempt to submit form. | Validation error message appears preventing submission.         |
| ContactSalesBtn_10 | Verify form submission with valid inputs completes successfully and shows a confirmation message. | 1. Fill all required fields with valid data. 2. Submit the form. | Form submits successfully; confirmation or thank-you message appears. |
| ContactSalesBtn_11 | Verify form reset/clear functionality                    | 1. Enter data in form. 2. Click reset/clear button.    | All entered data is cleared from form fields.                   |
| ContactSalesBtn_12 | Verify phone number field accepts valid input only      | 1. Enter letters or special characters in phone number field. 2. Attempt to submit form. | Validation blocks submission or shows error for invalid phone input. |
| ContactSalesBtn_13 | Verify privacy policy / terms link presence and function | 1. Locate and click privacy policy or terms link near form. | Link opens relevant document/page in new tab/window.            |
| ContactSalesBtn_14 | Verify captcha or anti-bot feature works and prevents spam submissions. | 1. Try to submit form without completing captcha.       | Submission blocked; prompts user to complete captcha.           |
| ContactSalesBtn_15 | Verify the Contact Sales page renders correctly on various devices | 1. Open page on desktop, tablet, and mobile or simulate different screen sizes. | Layout adjusts properly; no broken or overlapping elements.     |
| ContactSalesBtn_16 | Verify accessibility compliance Verify the page and form are accessible (keyboard navigation, screen readers). | 1. Navigate form using keyboard only. 2. Check screen reader labels and alt text for images. | Page and form are fully accessible without mouse.               |

---

### Trial Input Button Test Cases (Trial_Input_Btn)

| Test Case ID        | Test Case Description                                  | Steps to Execute                                        | Expected Result                               |
|---------------------|-------------------------------------------------------|--------------------------------------------------------|----------------------------------------------|
| Trial_Input_Btn_01   | Verify "Email Address" input field is present on homepage | Navigate to OrangeHRM homepage Check for the presence of the email input field. | Email input field is visible and enabled for input. |
| Trial_Input_Btn_02   | Verify that the email input field has placeholder text indicating what to enter. | Observe the email input field before typing.           | Placeholder text like "Enter your email" or similar is visible. |
| Trial_Input_Btn_03   | Verify valid email is accepted in "Email Address" input field | Click the email input field. Type a valid email address (e.g., user@example.com). | Text is entered correctly without issues.    |
| Trial_Input_Btn_04   | Verify invalid email is rejected in "Email Address" input field | Enter invalid email (e.g., test@, abc) and click "Start 30 Days Free Trial" button | Inline validation error message is shown.     |
| Trial_Input_Btn_05  | Verify empty email field cannot be submitted using "Start 30 Days Free Trial" button | Leave the "Email Address" field blank and click the "Start 30 Days Free Trial" button | Form does not submit; error shown                        |
| Trial_Input_Btn_06  | Verify that the email input field restricts input to a reasonable maximum length (e.g., 254 characters). | Try entering an email longer than 254 characters.            | Input is restricted or trimmed, preventing overflow.    |
| Trial_Input_Btn_07  | Verify "Start 30 Days Free Trial" button is present and clickable  | Open the free trial page. Locate the button near the email input field. | Button is visible and labeled “Start 30 Days Free Trial” |
| Trial_Input_Btn_08  | Verify clicking "Start 30 Days Free Trial" button with valid email redirects to trial form | Enter a valid email address. Click the button.               | Redirected to https://www.orangehrm.com/en/30-day-free-trial |
| Trial_Input_Btn_09  | Verify clicking "Start 30 Days Free Trial" button with invalid email does not redirect | Enter an invalid email address. Click the button.            | Stays on same page, error shown                          |
| Trial_Input_Btn_10  | Verify the button is enabled only when a valid email is entered.   | Enter a valid email address. Observe the button state.       | The button becomes enabled and clickable.               |
| Trial_Input_Btn_11  | Verify the "30 Day Free Trial" button is disabled if the email input is empty | Leave the email field empty. Observe the button state.       | The button is disabled or clicking it shows an error preventing submission. |
| Trial_Input_Btn_12  | Verify trial form page loads after clicking "Start 30 Days Free Trial" button | 1. Enter a valid email on homepage 2. Click the button to start free trial | The 30 Days Free Trial page loads without errors        |
| Trial_Input_Btn_13  | Verify that clicking the button with an invalid email does not proceed and shows an error. | Enter an invalid email format. Click the button.             | The form is not submitted, and an error message appears prompting a valid email. |

---

### Trial Page Form Test Cases (TrialPage)

| Test Case ID       | Test Case Description                                            | Steps to Execute                                    | Expected Result                                   |
|--------------------|-----------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| TrialPage_01       | Verify "Start Your Free Trial" header is displayed on trial page | Observe header                                     | Header text is present and correct                |
| TrialPage_02       | Verify all required input fields are present: User Name, Full Name, Business Email, Phone Number, Country | Load form page                                     | All fields are visible                             |
| TrialPage_03       | Verify validation for "User Name" input field                   | Leave blank and click "Get Your Free Trial" button | Error message shown below the field                |
| TrialPage_04       | Verify validation for "Full Name" input field                   | Leave blank and click "Get Your Free Trial" button | Error message shown                                |
| TrialPage_05       | Verify validation for "Business Email" input field              | Enter invalid email and click submit               | Error message like “Enter valid email” shown      |
| TrialPage_06       | Verify email entered on homepage is prefilled in "Business Email" input field on trial page | Enter email on homepage → redirect                 | Prefilled or visible in form (if supported)       |
| TrialPage_07       | Verify validation for "Phone Number" input field                | Enter letters or symbols                            | Error message shown, only digits allowed           |
| TrialPage_08       | Verify "Country" dropdown is present and functional             | Open the dropdown                                  | Country list is visible and selectable             |
| TrialPage_09       | Verify "Terms and Conditions" checkbox is required before clicking "Get Your Free Trial" button | Try submitting without checking the box            | Form submission blocked                             |
| TrialPage_10       | Verify successful form submission with all valid inputs and "Get Your Free Trial" button | Fill all fields, check T&C, click "Get Your Free Trial" | Success message or redirect to dashboard          |
| TrialPage_11       | Verify incomplete form blocks submission when "Full Name" or others are empty | Leave one field blank                               | Validation error prevents form submission          |
| TrialPage_12       | Verify invalid email or phone number prevents clicking "Get Your Free Trial" | Enter wrong formats                                | Field-specific error shown                          |
| TrialPage_13       | Verify duplicate email in "Business Email" field shows error    | Use already used email                              | Message like “Email already registered”            |
| TrialPage_14       | Verify behavior when backend returns server error on "Get Your Free Trial" click | Simulate server error                              | User-friendly error like “Something went wrong”    |
| TrialPage_15       | Verify CAPTCHA (if present) is required before clicking "Get Your Free Trial" button | Skip CAPTCHA and click                              | Form not submitted (if applicable)                  |
| TrialPage_16       | Verify no page refresh occurs when "Get Your Free Trial" button is clicked | Observe page behavior                              | Page remains static, only shows success/errors dynamically (AJAX-based) |
| TrialPage_17       | Verify labels for all form fields: “Full Name”, “User Name”, “Business Email”, etc. | Review form layout                                 | Labels are descriptive and positioned correctly    |
| TrialPage_18       | Verify Tab key navigates through form inputs in correct order   | Press Tab from first field                          | Cursor moves in logical order                        |
| TrialPage_19       | Verify mobile responsiveness of trial page and form             | Open on mobile device                              | Form scales properly and is usable                   |
| TrialPage_20       | Verify privacy and security note is displayed near "Get Your Free Trial" button | Observe form page                                  | Text like “Your information is safe” is visible     |

---

### Homepage Test Cases (HP)

| Test Case ID | Test Case Description                  | Steps to Execute                       | Expected Result              |
|--------------|--------------------------------------|-------------------------------------|-----------------------------|
| HP-003       | Verify embedded video is present and playable | Find embedded YouTube video, click play | Video plays without issues  |
| HP-004       | Verify top navigation menu presence   | Load homepage                       | Menu is visible             |
| HP-005       | Verify dropdown appears on hovering/clicking 'Platform' | Hover/click 'Platform' menu          | Dropdown menu is displayed  |
| HP-006       | Verify customer logos are visible     | Scroll to Social Proof section      | Logos of companies are displayed |
| HP-007       | Verify customer testimonials are visible | Scroll to testimonials section      | Testimonials are present and readable |

---

### People Management Section Test Cases (PM)

| Test Case ID | Test Case Description                                                  | Steps to Execute                              | Expected Result                                                                 |
|--------------|------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------|
| PM_01        | Verify the "People Management" section is present on the homepage or relevant page. | 1. Open OrangeHRM homepage 2. Scroll to find People Management section | People Management section is visible with relevant heading or text             |
| PM_02        | Verify Performance Management section is visible                       | Scroll to the Performance Management section on the homepage. | The Performance Management section is displayed clearly on the homepage.       |
| PM_03        | Verify section title text                                              | Read the heading/title of the section.        | Title should read "Performance Management".                                    |
| PM_04        | Verify icon/image loads in Performance Management section              | Check for the presence of icon/image next to the title or text. | The image/icon is visible and properly loaded.                                |
| PM_05        | Verify description content in Performance Management section           | Read the paragraph or description under the section. | Description is meaningful and relevant to Performance Management.             |
| PM_06        | Verify responsiveness of Performance Management section               | Open the homepage on mobile, tablet, and desktop devices. | Section adjusts correctly to all screen sizes.                                |
| PM_07        | Verify the "Learn More" button under People Management section is visible and clickable. | 1. Locate the Learn More button in the People Management section | Button is visible and clickable                                               |
| PM_08        | Verify clicking the Learn More button navigates to the correct HR Administration page. | 1. Click the Learn More button                 | Navigates to HR Administration page: https://www.orangehrm.com/en/solutions/people-management/hr-administration |
| PM_09        | Verify the URL after clicking Learn More matches exactly the expected URL. | 1. Click Learn More 2. Observe the browser address bar | URL matches exactly: https://www.orangehrm.com/en/solutions/people-management/hr-administration |
| PM_10        | Verify HR Administration page loads successfully                       | Navigate to the URL https://www.orangehrm.com/en/solutions/people-management/hr-administration or via Learn More button. | Page loads fully with no errors, broken links, or missing content              |

---

### HR Administration Page Test Cases (HRP)

| Test Case ID | Test Case Description                                             | Steps to Execute                                           | Expected Result                          |
|--------------|-------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|
| HRP_01      | Verify the page title and main header text correctly reflect "HR Administration" or related terms. | Check the page title (browser tab). Check the main page heading. | Title and heading reflect "HR Administration" |
| HRP_02      | Verify presence of key content sections                           | 1. Scroll through page 2. Identify sections like Features, Benefits, CTAs | All expected content sections are present and correctly labeled |
| HRP_03      | Verify images and icons load correctly                            | 1. Visually inspect all images and icons                   | All images/icons are visible and not broken  |
| HRP_04      | Verify presence of Book a free Demo buttons                      | 1. Locate buttons like “Request a Demo,” “Contact Us,” etc.| CTA is visible and clickable             |
| HRP_05      | Verify that clicking Book a free Demo button takes the user to the correct next step/page/form. | 1. Click CTA buttons                                        | Navigates to the correct destination (form, contact page, etc.) |
| HRP_06      | Verify the HR Administration page is responsive on desktop, tablet, and mobile devices. | 1. Open in desktop, tablet, and mobile or use browser dev tools | Layout adjusts for all screen sizes, with no overlap or cutoff elements |
| HRP_07       | Verify navigation menu functionality                              | 1. Interact with main/top navigation bar          | Menu works correctly, all links functional                          |
| HRP_08       | Verify page load performance                                      | 1. Load page several times and measure speed      | Page loads in under 3 seconds (on average internet connection)     |
| HRP_09       | Verify that the page contains proper SEO metadata (meta title, description, keywords). | 1. Inspect page source or use SEO analysis tool    | Meta title, meta description, and keywords relevant to HR Administration are present |
| HRP_10       | Verify the page follows basic accessibility guidelines (alt text on images, keyboard navigable, etc.). | 1. Use accessibility audit tools 2. Try navigating with only keyboard | Alt text present, keyboard accessible, contrast sufficient         |

---

### Culture Management Section Test Cases (CM)

| Test Case ID | Test Case Description                    | Steps to Execute                              | Expected Result                                |
|--------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|
| CM_01        | Verify Culture Management section visibility | Scroll to the Culture Management section     | Section is visible on the homepage             |
| CM_02        | Verify section heading                   | Check the heading/title of the section        | Heading is correctly labeled as "Culture Management" |
| CM_03        | Verify icon/image is visible             | Check for any icon or image associated with the section | Image or icon is loaded and displayed properly |
| CM_04        | Verify description content               | Read the description/content under Culture Management | Description text is readable and relevant       |
| CM_05        | Verify Learn More button presence        | Check for a "Learn More" button in the section | A clearly labeled "Learn More" button is visible |
| CM_06        | Verify Learn More button is clickable    | Click the Learn More button                    | Button is clickable and responsive              |
| CM_07        | Verify Learn More button navigates correctly | Click the Learn More button                    | Browser navigates to: https://www.orangehrm.com/en/solutions/culture/performance-management |
| CM_08        | Verify responsive design of the section | Open page on mobile, tablet, and desktop      | Section adapts to screen size and displays properly |
| CM_09        | Verify accessibility (keyboard navigation) | Navigate section using the keyboard (Tab key) | All elements are accessible via keyboard        |
| CM_10        | Verify alt text or labels on images/icons | Inspect icons/images for alt or aria labels   | Proper alt/aria labels are present for accessibility |

---

### Performance Management Page Test Cases (PMP)

| Test Case ID | Test Case Description                        | Steps to Execute                               | Expected Result                                      |
|--------------|---------------------------------------------|-----------------------------------------------|-----------------------------------------------------|
| PMP_01       | Verify Performance Management Page loads successfully | Navigate to https://www.orangehrm.com/en/solutions/culture/performance-management | Page loads completely without errors                 |
| PMP_02       | Verify correct URL of Performance Management Page | Check the browser address bar                   | URL should exactly match the expected one            |
| PMP_03       | Verify title of Performance Management Page | View the browser tab title                       | Tab title is relevant to “Performance Management”    |
| PMP_04       | Verify main header of the Performance Management Page | Look at the main header/title on the page       | Header clearly mentions “Performance Management”      |
| PMP_05       | Verify content sections are present          | Scroll through the page and review all sections | Multiple informative sections related to performance management are visible |
| PMP_06       | Verify call-to-action buttons (e.g., Book a Demo) | Look for CTA buttons and click them              | Buttons are functional and lead to relevant pages or forms |
| PMP_07       | Verify images and icons load correctly        | Check for banners, icons, and any visual media  | All visuals load successfully without errors          |
| PMP_08       | Verify responsiveness of the Performance Management Page | Test page on desktop, tablet, and mobile         | Layout adjusts properly on all devices                 |
| PMP_09       | Verify keyboard accessibility                 | Use only the keyboard (Tab key) to navigate through the page | All interactive elements (links, buttons) are keyboard-navigable |

---

### Talent Management Section Test Cases (TM)

| Test Case ID  | Test Case Description                        | Steps to Execute                    | Expected Result                         |
|---------------|---------------------------------------------|-----------------------------------|----------------------------------------|
| TM_01         | Check visibility of the Talent Management section | Scroll to the Talent Management section | Section is visible on the homepage      |
| TM_02         | Check heading text in the Talent Management section | Inspect the heading                | Heading says "Talent Management" or relevant title |
| TM_03         | Check if the description is displayed       | Scroll to the section              | Description under heading is visible and readable |
| TM_04         | Check image/icon visibility in the section  | Locate the image/icon              | Icon/image is displayed without distortion |
| TM_05         | Check the "Learn More" button visibility    | Scroll to the Talent Management section | Button is visible and labeled correctly |
| TM_06         | Check button is clickable                     | Click on the “Learn More” button  | Button responds to the click             |
| TM_07         | Check redirection of "Learn More" button    | Click on the button                | User is redirected to: https://www.orangehrm.com/en/solutions/talent-management/recruitment |
| TM_08         | Check button hover state                      | Hover over the "Learn More" button | Button changes visually on hover (e.g., color change, underline) |

---

### Talent Management Recruitment Page Test Cases (TM_REC_P)

| Test Case ID    | Test Case Description                       | Steps to Execute                  | Expected Result                           |
|-----------------|--------------------------------------------|---------------------------------|------------------------------------------|
| TM_REC_P_01     | Verify page loads successfully              | Open the URL                     | Page loads without error                  |
| TM_REC_P_02     | Verify correct page title                   | Check browser tab title          | Title includes "Recruitment" or "Talent Management" |
| TM_REC_P_03     | Verify breadcrumb navigation exists         | Locate breadcrumb on page        | Breadcrumb shows correct navigation path |
| TM_REC_P_04     | Check main banner/heading visibility         | Check for main title at top of the page | Main heading "Recruitment" or similar is clearly visible |
| TM_REC_P_05     | Check banner image/video presence            | Locate banner section            | Banner image/video loads and displays correctly |
| TM_REC_P_06     | Check presence of key feature sections       | Scroll through page              | Sections like “Streamline Hiring”, “Custom Workflow”, etc., are visible |
| TM_REC_P_07     | Check for consistency in fonts and layout    | Inspect overall design           | Fonts, buttons, and layout are consistent and professional |
| TM_REC_P_08     | Verify "Book a Demo" button visibility       | Scroll and check page            | "Book a Demo" button appears on page     |
| TM_REC_P_09     | Verify "Book a Demo" redirection              | Click on "Book a Demo"           | Redirects to demo request form/page      |
| TM_REC_P_10     | Check images/icons for each feature block     | Scroll to feature sections       | Icons/images are present and visually clear |
| TM_REC_P_11     | Check for CTA (Call-To-Action) at bottom      | Scroll to the bottom             | CTA like “Contact Us”, “Demo”, or “Get Started” is available |
| TM_REC_P_12     | Check mobile responsiveness                    | Resize browser window or use device emulator | Page adapts layout properly for mobile    |
| TM_REC_P_13     | Check content spellings and grammar            | Review headings and paragraphs   | No spelling or grammar errors             |
| TM_REC_P_14     | Verify loading time performance                | Measure page load time           | Page loads in under 3 seconds              |
| TM_REC_P_15     | Check links in the page                         | Click on internal links (if any) | Links redirect to correct pages            |
| TM_REC_P_16     | Check page scroll behavior                      | Scroll up/down                  | Smooth scrolling, no glitches or stuck sections |
| TM_REC_P_17     | Check SEO metadata                              | View page source or inspect      | Meta title, description, and keywords are defined |
| TM_REC_P_18     | Test accessibility                              | Use accessibility tool or tab navigation | Page follows accessibility guidelines (labels, alt tags, keyboard navigation) |

---

### Footer Test Cases (Footer)

| Test Case ID | Test Case Description                  | Steps to Execute                     | Expected Result                      |
|--------------|--------------------------------------|------------------------------------|-------------------------------------|
| Footer_01    | Verify footer is visible on all pages | 1. Visit multiple pages (home, demo, contact). 2. Scroll to bottom. | Footer is visible on all pages consistently |
| Footer_02    | Verify all footer links are present              | 1. Inspect footer section. 2. Check presence of links like About Us, Contact, Careers, Terms, Privacy, etc. | All expected footer links are visible.                      |
| Footer_03    | Verify all footer links are clickable            | 1. Click each footer link.                                    | Each link is clickable and navigates to the correct page.  |
| Footer_04    | Verify social media icons are present             | 1. Look for social icons like Facebook, Twitter, LinkedIn, YouTube. | All expected social icons are displayed.                   |
| Footer_05    | Verify social media icons open correct URLs       | 1. Click each social icon. 2. Confirm redirection.            | User is redirected to respective social media pages in a new tab. |
| Footer_06    | Verify footer responsiveness on different screen sizes | 1. Resize browser (desktop, tablet, mobile). 2. Check footer layout. | Footer adjusts layout properly for each screen size.       |
| Footer_07    | Verify copyright information                      | 1. View footer section. 2. Check copyright text.              | Correct copyright info (e.g., © 2025 OrangeHRM) is shown.  |
| Footer_08    | Verify Terms & Conditions link works              | 1. Click on "Terms & Conditions" in footer.                   | Navigates to the Terms & Conditions page.                   |
| Footer_09    | Verify Privacy Policy link works                   | 1. Click on "Privacy Policy" in footer.                        | Navigates to the Privacy Policy page.                       |
| Footer_10    | Verify footer links open in new tab                | 1. Click external links (social media, legal).                 | External links open in a new browser tab/window.            |
| Footer_11    | Verify footer accessibility via keyboard           | 1. Use Tab key to navigate to footer. 2. Verify focus indicators on links/icons. | All links/icons are focusable and keyboard accessible.      |
| Footer_12    | Verify footer elements have appropriate alt text or ARIA labels | 1. Use a screen reader to inspect footer.                      | All icons and links have descriptive text or ARIA labels.  |
| Footer_14    | Verify validation for invalid email in newsletter field | 1. Enter invalid email and submit.                             | Validation error shown.                                     |
