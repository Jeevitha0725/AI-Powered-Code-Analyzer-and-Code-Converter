       IDENTIFICATION DIVISION.
       PROGRAM-ID. TABLE-OPERATIONS.
       
       ENVIRONMENT DIVISION.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
      * First table - Employee details
       01 EMPLOYEE-TABLE.
          05 EMP-RECORD OCCURS 5 TIMES INDEXED BY EMP-IDX.
             10 EMP-ID              PIC 9(5).
             10 EMP-NAME            PIC X(20).
             10 EMP-DEPT            PIC X(10).
             10 EMP-SALARY          PIC 9(7)V99.
             
      * Second table - Department details     
       01 DEPARTMENT-TABLE.
          05 DEPT-RECORD OCCURS 3 TIMES INDEXED BY DEPT-IDX.
             10 DEPT-ID             PIC X(10).
             10 DEPT-NAME           PIC X(20).
             10 DEPT-LOCATION       PIC X(15).
             
      * Combined table - Employee Department Details
       01 EMP-DEPT-TABLE.
          05 EMP-DEPT-RECORD OCCURS 5 TIMES INDEXED BY COMB-IDX.
             10 COMB-EMP-ID         PIC 9(5).
             10 COMB-EMP-NAME       PIC X(20).
             10 COMB-DEPT-NAME      PIC X(20).
             10 COMB-LOCATION       PIC X(15).
             10 COMB-SALARY         PIC 9(7)V99.
             
      * Counter and temporary variables     
       01 WS-COUNTERS.
          05 I                      PIC 9(2) VALUE 1.
          05 J                      PIC 9(2) VALUE 1.
          
       01 WS-TEMP-SALARY           PIC 9(7)V99.
       01 WS-HIGHEST-SALARY        PIC 9(7)V99.
       01 WS-DEPT-TOTAL            PIC 9(8)V99.
       
       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM INITIALIZE-EMPLOYEE-TABLE
           PERFORM INITIALIZE-DEPARTMENT-TABLE
           PERFORM COMBINE-TABLES
           PERFORM CALCULATE-DEPT-TOTALS
           PERFORM FIND-HIGHEST-SALARY
           STOP RUN.
           
       INITIALIZE-EMPLOYEE-TABLE.
           MOVE 10001 TO EMP-ID(1)
           MOVE "John Smith" TO EMP-NAME(1)
           MOVE "IT" TO EMP-DEPT(1)
           MOVE 50000.00 TO EMP-SALARY(1)
           
           MOVE 10002 TO EMP-ID(2)
           MOVE "Jane Doe" TO EMP-NAME(2)
           MOVE "HR" TO EMP-DEPT(2)
           MOVE 45000.00 TO EMP-SALARY(2)
           
           MOVE 10003 TO EMP-ID(3)
           MOVE "Bob Wilson" TO EMP-NAME(3)
           MOVE "IT" TO EMP-DEPT(3)
           MOVE 55000.00 TO EMP-SALARY(3)
           
           MOVE 10004 TO EMP-ID(4)
           MOVE "Mary Johnson" TO EMP-NAME(4)
           MOVE "FIN" TO EMP-DEPT(4)
           MOVE 60000.00 TO EMP-SALARY(4)
           
           MOVE 10005 TO EMP-ID(5)
           MOVE "Steve Davis" TO EMP-NAME(5)
           MOVE "HR" TO EMP-DEPT(5)
           MOVE 48000.00 TO EMP-SALARY(5).
           
       INITIALIZE-DEPARTMENT-TABLE.
           MOVE "IT" TO DEPT-ID(1)
           MOVE "Information Tech" TO DEPT-NAME(1)
           MOVE "New York" TO DEPT-LOCATION(1)
           
           MOVE "HR" TO DEPT-ID(2)
           MOVE "Human Resources" TO DEPT-NAME(2)
           MOVE "Chicago" TO DEPT-LOCATION(2)
           
           MOVE "FIN" TO DEPT-ID(3)
           MOVE "Finance" TO DEPT-NAME(3)
           MOVE "Boston" TO DEPT-LOCATION(3).
           
       COMBINE-TABLES.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
              SET EMP-IDX TO I
              PERFORM VARYING J FROM 1 BY 1 UNTIL J > 3
                 SET DEPT-IDX TO J
                 IF EMP-DEPT(I) = DEPT-ID(J)
                    MOVE EMP-ID(I) TO COMB-EMP-ID(I)
                    MOVE EMP-NAME(I) TO COMB-EMP-NAME(I)
                    MOVE DEPT-NAME(J) TO COMB-DEPT-NAME(I)
                    MOVE DEPT-LOCATION(J) TO COMB-LOCATION(I)
                    MOVE EMP-SALARY(I) TO COMB-SALARY(I)
                 END-IF
              END-PERFORM
           END-PERFORM.
           
       CALCULATE-DEPT-TOTALS.
           MOVE ZEROS TO WS-DEPT-TOTAL
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
              IF EMP-DEPT(I) = "IT"
                 ADD EMP-SALARY(I) TO WS-DEPT-TOTAL
              END-IF
           END-PERFORM
           DISPLAY "IT Department Total Salary: " WS-DEPT-TOTAL
           
           MOVE ZEROS TO WS-DEPT-TOTAL
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
              IF EMP-DEPT(I) = "HR"
                 ADD EMP-SALARY(I) TO WS-DEPT-TOTAL
              END-IF
           END-PERFORM
           DISPLAY "HR Department Total Salary: " WS-DEPT-TOTAL.
           
       FIND-HIGHEST-SALARY.
           MOVE 0 TO WS-HIGHEST-SALARY
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
              IF EMP-SALARY(I) > WS-HIGHEST-SALARY
                 MOVE EMP-SALARY(I) TO WS-HIGHEST-SALARY
              END-IF
           END-PERFORM
           DISPLAY "Highest Salary: " WS-HIGHEST-SALARY.
