CREATE TABLE IF NOT EXISTS Salesman (
    id INT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commision REAL
);
INSERT INTO Salesman (id, name, city, Commision) VALUES
(1, 'John Doe', 'New York', 0.10),
(2, 'Jane Smith', 'Los Angeles', 0.12),
(3, 'Mike Johnson', 'Chicago', 0.08),
(4, 'Emily Davis', 'Houston', 0.15),
(5, 'David Wilson', 'Phoenix', 0.09),
(6, 'Sarah Brown', 'Philadelphia', 0.11);
SELECT * FROM Salesman;
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    p_amt REAL,
    o_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);