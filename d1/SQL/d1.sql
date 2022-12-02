CREATE TABLE Calories (value VARCHAR(10))
CREATE TABLE TotCalories (total INT)

BULK INSERT Calories
FROM 'path\to\file\input.txt'
WITH (
  ROWTERMINATOR = '\n',
  FIRSTROW = 0
)

DECLARE @MyCursor CURSOR;
DECLARE @MyField VARCHAR(MAX);
DECLARE @SUM INT
SET @SUM = 0
BEGIN
	SET @MyCursor = CURSOR FOR SELECT * FROM Calories   
    OPEN @MyCursor 
    FETCH NEXT FROM @MyCursor 
    INTO @MyField
    WHILE @@FETCH_STATUS = 0
    BEGIN
		IF @MyField IS NULL 
		BEGIN
			INSERT INTO TotCalories VALUES (@SUM)
			SET @SUM = 0
		END
		ELSE
		BEGIN
			SET @SUM = @SUM + CONVERT(INT, @MyField)
		END
      FETCH NEXT FROM @MyCursor 
      INTO @MyField 
    END; 
    CLOSE @MyCursor ;
    DEALLOCATE @MyCursor;
END

SELECT TOP 1 total as MAX FROM TotCalories
ORDER BY total DESC

SELECT SUM(t.total) AS 'SUM MAX ELEMENTS' FROM (
SELECT TOP 3 total FROM TotCalories
ORDER BY total DESC) AS t

