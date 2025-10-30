# Reflection on Static Code Analysis Lab

1)Which issues were the easiest to fix, and which were the hardest? Why?**

- The easiest to fix were style-related issues such as naming conventions, missing docstrings, and blank line formatting because they involve straightforward text changes.
- The hardest issue was the removal of unsafe usage of `eval()` since it required assessing the security risk and finding safe alternatives or removing unnecessary code.

2)Did the static analysis tools report any false positives? If so, describe one example.**

- Pylint sometimes flagged the use of the `global` statement as a warning, which was acceptable in this small script context, so it can be considered a false positive for this use case.

3)How would you integrate static analysis tools into your actual software development workflow?**

- I would include Pylint, Bandit, and Flake8 as part of a pre-commit hook to catch issues locally before committing.
- Additionally, integrate these tools in the CI/CD pipeline (e.g., GitHub Actions) to enforce code quality on every pull request.

4)What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

- Code readability improved greatly with proper naming, docstrings, and consistent formatting.
- Input validation and exception handling improved robustness by preventing crashes.
- Use of logging instead of print and removal of unsafe constructs increased security and maintainability.
