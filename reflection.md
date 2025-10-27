1.	Which issues were the easiest to fix, and which were the hardest? Why?
- The easiest issues were renaming functions to snake_case, removing unused imports, and adding missing docstrings.
- The hardest was removing the global statement without breaking the logic, which I fixed by updating the dictionary in place instead of reassigning it.


2.	Did the static analysis tools report any false positives? If so, describe one example.
- No major false positives were found.
- The global warning could be seen as minor, but addressing it still improved the code structure.


3.	How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
- I would integrate Pylint, Flake8, and Bandit into a CI/CD pipeline and use pre-commit hooks.
- This would ensure that code quality, style, and security checks happen automatically before commits or merges.


4.	What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- The code became cleaner, safer, and easier to maintain.
- Security risks like eval() and bare except were removed, file handling is safer with context managers, and it now scores 10/10 on Pylint with no Bandit or Flake8 issues.