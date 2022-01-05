# Key Takeaways 

- Ease of adding new features with the Open Closed Principle. 
    - Always remember: "Software components should be closed for modification, but open for extension" 
    - Assume we do not follow Open close. For all additional features we will have to start modifying the existing code, for all the number of changes/increase in frequency of changes we run the risk of creating bugs. 

- Leads to minimal cost of developing and testing software
    - The more time we need to spend on testing and quality assurance to prevent the bugs. With Open Close we still need to test, but testing a new piece of existing code is easier and more efficient than running a QA and regression test on the total code. 

- Open Closed Principle often requires decoupling, which, in turn, automatically follows the Single Responsibility Principle. 
    - Ended up with components that are following SRP because it AIMS AT LOOSE COUPLING 


# CAUTION
- DO NOT FOLLOW OPEN CLOSED PRINCIPLES BLINDLY 
- YOU WILL END UP WITH A HUGE NUMBER OF CLASSES THAT CAN COMPLICATE YOUR OVERALL DESIGN 
    - IF YOU THINK THE EXISTING CODE NEEDS TO BE MODIFIED FOR THE BUG THEN GO BACK AND CHANGE. IF YOU SEE A LOT OF BUGS YOU CAN THINK ABOUT GOING BACK TO RE-DESIGN 
