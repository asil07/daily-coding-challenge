
SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;


-- 1. **`SELECT player_id, MIN(event_date)`**:
--    - Select the `player_id` column and the minimum `event_date` for each player.

-- 2. **`FROM Activity`**:
--    - Query data from the `Activity` table.

-- 3. **`GROUP BY player_id`**:
--    - Group the rows by `player_id` so that the aggregate function `MIN(event_date)` calculates the earliest login date for each player.

-- ### Example Output:
-- For the input `Activity` table:

-- | player_id | device_id | event_date | games_played |
-- |-----------|-----------|------------|--------------|
-- | 1         | 2         | 2016-03-01 | 5            |
-- | 1         | 2         | 2016-05-02 | 6            |
-- | 2         | 3         | 2017-06-25 | 1            |
-- | 3         | 1         | 2016-03-02 | 0            |
-- | 3         | 4         | 2018-07-03 | 5            |

-- The output will be:

-- | player_id | first_login |
-- |-----------|-------------|
-- | 1         | 2016-03-01  |
-- | 2         | 2017-06-25  |
-- | 3         | 2016-03-02  |