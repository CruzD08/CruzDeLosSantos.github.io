-- ============================================================
-- Cultural Compass Travel Agency - Database Setup
-- Flask + MySQL Project
-- ============================================================

-- Create the database
CREATE DATABASE IF NOT EXISTS travel_agency;
USE travel_agency;

-- ============================================================
-- Table: packages
-- Stores travel packages offered by the agency
-- ============================================================
CREATE TABLE IF NOT EXISTS packages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    destination VARCHAR(200) NOT NULL,
    description TEXT,
    duration VARCHAR(50),
    price DECIMAL(10, 2),
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- Table: bookings
-- Stores booking requests submitted by users
-- ============================================================
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL,
    travel_date DATE,
    num_travelers INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE SET NULL
);

-- ============================================================
-- Table: comments
-- Stores user comments on travel packages
-- ============================================================
CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT,
    username VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);

-- ============================================================
-- Table: contacts
-- Stores messages submitted through the contact form
-- ============================================================
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL,
    subject VARCHAR(300),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- Sample Data: Travel Packages
-- ============================================================
INSERT INTO packages (title, destination, description, duration, price, image_url) VALUES
(
    'Lantern Festival Experience',
    'Chiang Mai, Thailand',
    'Experience the magical Yi Peng Lantern Festival in Chiang Mai. Watch thousands of lanterns float into the night sky while enjoying Thai cuisine, temple tours, and cultural workshops. This package includes guided tours of Doi Suthep temple, a Thai cooking class, and VIP seating at the lantern release ceremony.',
    '7 days / 6 nights',
    1299.99,
    'https://images.unsplash.com/photo-1514222134-b57cbb8ce073?w=800'
),
(
    'Cherry Blossom Season',
    'Tokyo & Kyoto, Japan',
    'Witness the stunning cherry blossom season across Japan. Visit iconic spots like Ueno Park, Philosopher''s Path, and Osaka Castle Park. Includes a traditional tea ceremony, kimono rental experience, and bullet train passes between cities.',
    '10 days / 9 nights',
    2499.99,
    'https://images.unsplash.com/photo-1522383225653-ed111181a951?w=800'
),
(
    'Seoul & Busan Adventure',
    'Seoul & Busan, South Korea',
    'Explore the vibrant culture of South Korea! Visit Gyeongbokgung Palace, Bukchon Hanok Village, and the bustling streets of Myeongdong in Seoul. Then head to Busan for Haeundae Beach, Gamcheon Culture Village, and fresh seafood at Jagalchi Market.',
    '12 days / 11 nights',
    1899.99,
    'https://images.unsplash.com/photo-1538485399081-7191377e8241?w=800'
),
(
    'Carnival in Rio',
    'Rio de Janeiro, Brazil',
    'Join the world''s biggest party at Rio Carnival! Dance to samba rhythms, watch the spectacular parade at the Sambadrome, and explore Rio''s iconic landmarks including Christ the Redeemer and Sugarloaf Mountain. Includes parade tickets and a samba dance class.',
    '6 days / 5 nights',
    1599.99,
    'https://images.unsplash.com/photo-1516306580123-e6e52b1b7b5f?w=800'
),
(
    'Holi Festival of Colors',
    'Jaipur & Delhi, India',
    'Celebrate Holi, the Festival of Colors, in the heart of India. Experience the joy of color-throwing celebrations, visit the Taj Mahal, explore Jaipur''s Pink City, and savor authentic Indian cuisine. A truly transformative cultural adventure.',
    '8 days / 7 nights',
    1199.99,
    'https://images.unsplash.com/photo-1576398289164-c48dc021b4e1?w=800'
),
(
    'Northern Lights & Ice Festival',
    'Harbin & Beijing, China',
    'Marvel at the Harbin Ice and Snow Festival, the world''s largest ice festival, featuring massive illuminated ice sculptures. Then explore Beijing''s Great Wall, Forbidden City, and vibrant hutong neighborhoods. A winter wonderland adventure.',
    '9 days / 8 nights',
    1799.99,
    'https://images.unsplash.com/photo-1548919973-5cef591cdbc9?w=800'
);

-- ============================================================
-- Sample Data: Comments
-- ============================================================
INSERT INTO comments (package_id, username, message) VALUES
(1, 'AdventureAmy', 'This looks amazing! Who else is going to the Lantern Festival? Would love to meet fellow travelers!'),
(1, 'TravelWithMike', 'I went last year and it was INCREDIBLE. The lantern release ceremony gave me chills. Highly recommend!'),
(3, 'KoreanCultureFan', 'Seoul is my favorite city! The street food in Myeongdong alone is worth the trip.'),
(3, 'FirstTimeTraveler', 'Hey! Who''s joining the Korea trip? This would be my first international trip and I''m so excited!'),
(2, 'SakuraLover', 'Cherry blossom season in Japan is a dream. The Philosopher''s Path in Kyoto is breathtaking.'),
(4, 'DancingQueen', 'Rio Carnival is on my bucket list! Anyone want to be travel buddies?');
