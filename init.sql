CREATE TABLE bus_schedule (
    id SERIAL PRIMARY KEY,
    route_id INT NOT NULL,
    departure_stop VARCHAR(100) NOT NULL,
    arrival_stop VARCHAR(100) NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL
);

INSERT INTO bus_schedule (route_id, departure_stop, arrival_stop, departure_time, arrival_time) VALUES
(1, 'City Center', 'North Station', '08:00', '10:00'),
(1, 'North Station', 'City Center', '10:30', '12:30'),
(2, 'West End', 'East Side', '09:00', '11:00'),
(2, 'East Side', 'West End', '11:30', '13:30'),
(3, 'South Square', 'Downtown', '07:30', '09:00'),
(3, 'Downtown', 'South Square', '09:30', '11:00'),
(4, 'Central Plaza', 'Industrial Park', '08:15', '09:00'),
(4, 'Industrial Park', 'Central Plaza', '09:30', '10:15'),
(5, 'Seaside Terminal', 'Mountain View', '07:00', '09:00'),
(5, 'Mountain View', 'Seaside Terminal', '09:30', '11:30');
