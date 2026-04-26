1. Python runs code top to bottom (line by line)
2. Execution starts from the first executable line 
3. A function runs only when it is called
4. when a function of other file gets imported :
   -> Python opens that file first
   -> Executes it completely once
   -> Then loads the function
   -> Then continues your main file
5. During import:
   -> function definitions do not run
   -> but normal code(input, print, function calls) runs immediately
6. To stop this unwanted execution, use: 
   **__name__ == "__main__":
7. Meanig of __name__:
   -> if file runs directly(itself) "__main__"
   ->if file is imported in other then "filename"
8. So:
   ->Direct run -> code inside __main__ runs
   ->Import -> code inside __main__ is skipped for that file , because that will call the function it needs not the whole unnecessary code it want of the imported file
9. __main__ only controls when code runs, not function access
10. Functions can still be called from other files even if inside same file
11. import executes file only once per run
12. if imported again in same program -> it uses cache (does not run again)
13. if you run program again -> everything start fresh and runs again
14. python must execute import first because it needs to know the function before using it.
15. This is called short-circuit evaluation
