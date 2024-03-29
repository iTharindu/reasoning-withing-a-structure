from nltk import *
from nltk.sem.drt import DrtParser
from nltk.sem import logic
import nltk
from nltk.sem import Expression
from nltk import load_parser
from nltk.sem import Valuation, Model
from nltk.corpus import brown


import random
import re

import numpy as np
import pandas as pd

from nltk.parse.generate import generate

import inflect

plural = inflect.engine()


male_names = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Alexander', 'Henry', 'Jacob', 'Michael', 'Daniel', 'Logan', 'Jackson', 'Sebastian', 'Jack', 'Aiden', 'Owen', 'Samuel', 'Matthew', 'Joseph', 'Levi', 'Mateo', 'David', 'John', 'Wyatt', 'Carter', 'Julian', 'Luke', 'Grayson', 'Isaac', 'Jayden', 'Theodore', 'Gabriel', 'Anthony', 'Dylan', 'Leo', 'Lincoln', 'Jaxon', 'Asher', 'Christopher', 'Josiah', 'Andrew', 'Thomas', 'Joshua', 'Ezra', 'Hudson', 'Charles', 'Caleb', 'Isaiah', 'Ryan', 'Nathan', 'Adrian', 'Christian', 'Maverick', 'Colton', 'Elias', 'Aaron', 'Eli', 'Landon', 'Jonathan', 'Nolan', 'Hunter', 'Cameron', 'Connor', 'Santiago', 'Jeremiah', 'Ezekiel', 'Angel', 'Roman', 'Easton', 'Miles', 'Robert', 'Jameson', 'Nicholas', 'Greyson', 'Cooper', 'Ian', 'Carson', 'Axel', 'Jaxson', 'Dominic', 'Leonardo', 'Luca', 'Austin', 'Jordan', 'Adam', 'Xavier', 'Jose', 'Jace', 'Everett', 'Declan', 'Evan', 'Kayden', 'Parker', 'Wesley', 'Kai', 'Brayden', 'Bryson', 'Weston', 'Jason', 'Emmett', 'Sawyer', 'Silas', 'Bennett', 'Brooks', 'Micah', 'Damian', 'Harrison', 'Waylon', 'Ayden', 'Vincent', 'Ryder', 'Kingston', 'Rowan', 'George', 'Luis', 'Chase', 'Cole', 'Nathaniel', 'Zachary', 'Ashton', 'Braxton', 'Gavin', 'Tyler', 'Diego', 'Bentley', 'Amir', 'Beau', 'Gael', 'Carlos', 'Ryker', 'Jasper', 'Max', 'Juan', 'Ivan', 'Brandon', 'Jonah', 'Giovanni', 'Kaiden', 'Myles', 'Calvin', 'Lorenzo', 'Maxwell', 'Jayce', 'Kevin', 'Legend', 'Tristan', 'Jesus', 'Jude', 'Zion', 'Justin', 'Maddox', 'Abel', 'King', 'Camden', 'Elliott', 'Malachi', 'Milo', 'Emmanuel', 'Karter', 'Rhett', 'Alex', 'August', 'River', 'Xander', 'Antonio', 'Brody', 'Finn', 'Elliot', 'Dean', 'Emiliano', 'Eric', 'Miguel', 'Arthur', 'Matteo', 'Graham', 'Alan', 'Nicolas', 'Blake', 'Thiago', 'Adriel', 'Victor', 'Joel', 'Timothy', 'Hayden', 'Judah', 'Abraham', 'Edward', 'Messiah', 'Zayden', 'Theo', 'Tucker', 'Grant', 'Richard', 'Alejandro', 'Steven', 'Jesse', 'Dawson', 'Bryce', 'Avery', 'Oscar', 'Patrick', 'Archer', 'Barrett', 'Leon', 'Colt', 'Charlie', 'Peter', 'Kaleb', 'Lukas', 'Beckett', 'Jeremy', 'Preston', 'Enzo', 'Luka', 'Andres', 'Marcus', 'Felix', 'Mark', 'Ace', 'Brantley', 'Atlas', 'Remington', 'Maximus', 'Matias', 'Walker', 'Kyrie', 'Griffin', 'Kenneth', 'Israel', 'Javier', 'Kyler', 'Jax', 'Amari', 'Zane', 'Emilio', 'Knox', 'Adonis', 'Aidan', 'Kaden', 'Paul', 'Omar', 'BrianPeter', 'Louis', 'Caden', 'Maximiliano', 'Holden', 'Paxton', 'Nash', 'Bradley', 'Bryan', 'Simon', 'Phoenix', 'Lane', 'Josue', 'Colin', 'Rafael', 'Kyle', 'Riley', 'Jorge', 'Beckham', 'Cayden', 'Jaden', 'Emerson', 'Ronan', 'Karson', 'Arlo', 'Tobias', 'Brady', 'Clayton', 'Francisco', 'Zander', 'Erick', 'Walter', 'Daxton', 'Martin', 'Damien', 'Dallas', 'Cody', 'Chance', 'Jensen', 'Finley', 'Jett', 'Corbin', 'Kash', 'Reid', 'Kameron', 'Andre', 'Gunner', 'Jake', 'Hayes', 'Manuel', 'Prince', 'Bodhi', 'Cohen', 'Sean', 'Khalil', 'Hendrix', 'Derek', 'Cristian', 'Cruz', 'Kairo', 'Dante', 'Atticus', 'Killian', 'Stephen', 'Orion', 'Malakai', 'Ali', 'Eduardo', 'Fernando', 'Anderson', 'Angelo', 'Spencer', 'Gideon', 'Mario', 'Titus', 'Travis', 'Rylan', 'Kayson', 'Ricardo', 'Tanner', 'Malcolm', 'Raymond', 'Odin', 'Cesar', 'Lennox', 'Joaquin', 'Kane', 'Wade', 'Muhammad', 'Iker', 'Jaylen', 'Crew', 'Zayn', 'Hector', 'Ellis', 'Leonel', 'Cairo', 'Garrett', 'Romeo', 'Dakota', 'Edwin', 'Warren', 'Julius', 'Major', 'Donovan', 'Caiden', 'Tyson', 'Nico', 'Sergio', 'Nasir', 'Rory', 'Devin', 'Jaiden', 'Jared', 'Kason', 'Malik', 'Jeffrey', 'Ismael', 'Elian', 'Marshall', 'Lawson', 'Desmond', 'Winston', 'Nehemiah', 'Ari', 'Conner', 'Jay', 'Kade', 'Andy', 'Johnny', 'Jayceon', 'Marco', 'Seth', 'Ibrahim', 'Raiden', 'Collin', 'Edgar', 'Erik', 'Troy', 'Clark', 'Jaxton', 'Johnathan', 'Gregory', 'Russell', 'Royce', 'Fabian', 'Ezequiel', 'Noel', 'Pablo', 'Cade', 'Pedro', 'Sullivan', 'Trevor', 'Reed', 'Quinn', 'Frank', 'Harvey', 'Princeton', 'Zayne', 'Matthias', 'Conor', 'Sterling', 'Dax', 'Grady', 'Cyrus', 'Gage', 'Leland', 'Solomon', 'Emanuel', 'Niko', 'Ruben', 'Kasen', 'Mathias', 'Kashton', 'Franklin', 'Remy', 'Shane', 'Kendrick', 'Shawn', 'Otto', 'Armani', 'Keegan', 'Finnegan', 'Memphis', 'Bowen', 'Dominick', 'Kolton', 'Jamison', 'Allen', 'Philip', 'Tate', 'Peyton', 'Jase', 'Oakley', 'Rhys', 'Kyson', 'Adan', 'Esteban', 'Dalton', 'Gianni', 'Callum', 'Sage', 'Alexis', 'Milan', 'Moises', 'Jonas', 'Uriel', 'Colson', 'Marcos', 'Zaiden', 'Hank', 'Damon', 'Hugo', 'Ronin', 'Royal', 'Kamden', 'Dexter', 'Luciano', 'Alonzo', 'Augustus', 'Kamari', 'Eden', 'Roberto', 'Baker', 'Bruce', 'Kian', 'Albert', 'Frederick', 'Mohamed', 'Abram', 'Omari', 'Porter', 'Enrique', 'Alijah', 'Francis', 'Leonidas', 'Zachariah', 'Landen', 'Wilder', 'Apollo', 'Santino', 'Tatum', 'Pierce', 'Forrest', 'Corey', 'Derrick', 'Isaias', 'Kaison', 'Kieran', 'Arjun', 'Gunnar', 'Rocco', 'Emmitt', 'Abdiel', 'Braylen', 'Maximilian', 'Skyler', 'Phillip', 'Benson', 'Cannon', 'Deacon', 'Dorian', 'Asa', 'Moses', 'Ayaan', 'Jayson', 'Raul', 'Briggs', 'Armando', 'Nikolai', 'Cassius', 'Drew', 'Rodrigo', 'Raphael', 'Danny', 'Conrad', 'Moshe', 'Zyaire', 'Julio', 'Casey', 'Ronald', 'Scott', 'Callan', 'Roland', 'Saul', 'Jalen', 'Brycen', 'Ryland', 'Lawrence', 'Davis', 'Rowen', 'Zain', 'Ermias', 'Jaime', 'Duke', 'Stetson', 'Alec', 'Yusuf', 'Case', 'Trenton', 'Callen', 'Ariel', 'Jasiah', 'Soren', 'Dennis', 'Donald', 'Keith', 'Izaiah', 'Lewis', 'Kylan', 'Kobe', 'Makai', 'Rayan', 'Ford', 'Zaire', 'Landyn', 'Roy', 'Bo', 'Chris', 'Jamari', 'Ares', 'Mohammad', 'Darius', 'Drake', 'Tripp', 'Marcelo', 'Samson', 'Dustin', 'Layton', 'Gerardo', 'Johan', 'Kaysen', 'Keaton', 'Reece', 'Chandler', 'Lucca', 'Mack', 'Baylor', 'Kannon', 'Marvin', 'Huxley', 'Nixon', 'Tony', 'Cason', 'Mauricio', 'Quentin', 'Edison', 'Quincy', 'Ahmed', 'Finnley', 'Justice', 'Taylor', 'Gustavo', 'Brock', 'Ahmad', 'Kyree', 'Arturo', 'Nikolas', 'Boston', 'Sincere', 'Alessandro', 'Braylon', 'Colby', 'Leonard', 'Ridge', 'Trey', 'Aden', 'Leandro', 'Sam', 'Uriah', 'Ty', 'Sylas', 'Axton', 'Issac', 'Fletcher', 'Julien', 'Wells', 'Alden', 'Vihaan', 'Jamir', 'Valentino', 'Shepherd', 'Keanu', 'Hezekiah', 'Lionel', 'Kohen', 'Zaid', 'Alberto', 'Neil', 'Denver', 'Aarav', 'Brendan', 'Dillon', 'Koda', 'Sutton', 'Kingsley', 'Sonny', 'Alfredo', 'Wilson', 'Harry', 'Jaziel', 'Salvador', 'Cullen', 'Hamza', 'Dariel', 'Rex', 'Zeke', 'Mohammed', 'Nelson', 'Boone', 'Ricky', 'Santana', 'Cayson', 'Lance', 'Raylan', 'Lucian', 'Eliel', 'Alvin', 'Jagger', 'Braden', 'Curtis', 'Mathew', 'Jimmy', 'Kareem', 'Archie', 'Amos', 'Quinton', 'Yosef', 'Bodie', 'Jerry', 'Langston', 'Axl', 'Stanley', 'Clay', 'Douglas', 'Layne', 'Titan', 'Tomas', 'Houston', 'Darren', 'Lachlan', 'Kase', 'Korbin', 'Leighton', 'Joziah', 'Samir', 'Watson', 'Colten', 'Roger', 'Shiloh', 'Tommy', 'Mitchell', 'Azariah', 'Noe', 'Talon', 'Deandre', 'Lochlan', 'Joe', 'Carmelo', 'Otis', 'Randy', 'Byron', 'Chaim', 'Lennon', 'Devon', 'Nathanael', 'Bruno', 'Aryan', 'Flynn', 'Vicente', 'Brixton', 'Kyro', 'Brennan', 'Casen', 'Kenzo', 'Orlando', 'Castiel', 'Rayden', 'Ben', 'Grey', 'Jedidiah', 'Tadeo', 'Morgan', 'Augustine', 'Mekhi', 'Abdullah', 'Ramon', 'Saint', 'Emery', 'Maurice', 'Jefferson', 'Maximo', 'Koa', 'Ray', 'Jamie', 'Eddie', 'Guillermo', 'Onyx', 'Thaddeus', 'Wayne', 'Hassan', 'Alonso', 'Dash', 'Elisha', 'Jaxxon', 'Rohan', 'Carl', 'Kelvin', 'Jon', 'Larry', 'Reese', 'Aldo', 'Marcel', 'Melvin', 'Yousef', 'Aron', 'Kace', 'Vincenzo', 'Kellan', 'Miller', 'Jakob', 'Reign', 'Kellen', 'Kristopher', 'Ernesto', 'Briar', 'Gary', 'Trace', 'Joey', 'Clyde', 'Enoch', 'Jaxx', 'Crosby', 'Magnus', 'Fisher', 'Jadiel', 'Bronson', 'Eugene', 'Lee', 'Brecken', 'Atreus', 'Madden', 'Khari', 'Caspian', 'Ishaan', 'Kristian', 'Westley', 'Hugh', 'Kamryn', 'Musa', 'Rey', 'Thatcher', 'Alfred', 'Emory', 'Kye', 'Reyansh', 'Yahir', 'Cain', 'Mordechai', 'Zayd', 'Demetrius', 'Harley', 'Felipe', 'Louie', 'Branson', 'Graysen', 'Allan', 'Kole', 'Harold', 'Alvaro', 'Harlan', 'Amias', 'Brett', 'Khalid', 'Misael', 'Westin', 'Zechariah', 'Aydin', 'Kaiser', 'Lian', 'Bryant', 'Junior', 'Legacy', 'Ulises', 'Bellamy', 'Brayan', 'Kody', 'Ledger', 'Eliseo', 'Gordon', 'London', 'Rocky', 'Valentin', 'Terry', 'Damari', 'Trent', 'Bentlee', 'Canaan', 'Gatlin', 'Kiaan', 'Franco', 'Eithan', 'Idris', 'Krew', 'Yehuda', 'Marlon', 'Rodney', 'Creed', 'Salvatore', 'Stefan', 'Tristen', 'Adrien', 'Jamal', 'Judson', 'Camilo', 'Kenny', 'Nova', 'Robin', 'Rudy', 'Van', 'Bjorn', 'Brodie', 'Mac', 'Jacoby', 'Sekani', 'Vivaan', 'Blaine', 'Ira', 'Ameer', 'Dominik', 'Alaric', 'Dane', 'Jeremias', 'Kyng', 'Reginald', 'Bobby', 'Kabir', 'Jairo', 'Alexzander', 'Benicio', 'Vance', 'Wallace', 'Zavier', 'Billy', 'Callahan', 'Dakari', 'Gerald', 'Turner', 'Bear', 'Jabari', 'Cory', 'Fox', 'Harlem', 'Jakari', 'Jeffery', 'Maxton', 'Ronnie', 'Yisroel', 'Zakai', 'Bridger', 'Remi', 'Arian', 'Blaze', 'Forest', 'Genesis', 'Jerome', 'Reuben', 'Wesson', 'Anders', 'Banks', 'Calum', 'Dayton', 'Kylen', 'Dangelo', 'Emir', 'Malakhi', 'Salem', 'Blaise', 'Tru', 'Boden', 'Kolten', 'Kylo', 'Aries', 'Henrik', 'Kalel', 'Landry', 'Marcellus', 'Zahir', 'Lyle', 'Dario', 'Rene', 'Terrance', 'Xzavier', 'Alfonso', 'Darian', 'Kylian', 'Maison', 'Foster', 'Keenan', 'Yahya', 'Heath', 'Javion', 'Jericho', 'Aziel', 'Darwin', 'Marquis', 'Mylo', 'Ambrose', 'Anakin', 'Jordy', 'Juelz', 'Toby', 'Yael', 'Azrael', 'Brentley', 'Tristian', 'Bode', 'Jovanni', 'Santos', 'Alistair', 'Braydon', 'Kamdyn', 'Marc', 'Mayson', 'Niklaus', 'Simeon', 'Colter', 'Davion', 'Leroy', 'Ayan', 'Dilan', 'Ephraim', 'Anson', 'Merrick', 'Wes', 'Will', 'Jaxen', 'Maxim', 'Howard', 'Jad', 'Jesiah', 'Ignacio', 'Zyon', 'Ahmir', 'Jair', 'Mustafa', 'Jermaine', 'Yadiel', 'Aayan', 'Dhruv', 'Seven']


female_names = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 'Mia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Ella', 'Elizabeth', 'Camila', 'Luna', 'Sofia', 'Avery', 'Mila', 'Aria', 'Scarlett', 'Penelope', 'Layla', 'Chloe', 'Victoria', 'Madison', 'Eleanor', 'Grace', 'Nora', 'Riley', 'Zoey', 'Hannah', 'Hazel', 'Lily', 'Ellie', 'Violet', 'Lillian', 'Zoe', 'Stella', 'Aurora', 'Natalie', 'Emilia', 'Everly', 'Leah', 'Aubrey', 'Willow', 'Addison', 'Lucy', 'Audrey', 'Bella', 'Nova', 'Brooklyn', 'Paisley', 'Savannah', 'Claire', 'Skylar', 'Isla', 'Genesis', 'Naomi', 'Elena', 'Caroline', 'Eliana', 'Anna', 'Maya', 'Valentina', 'Ruby', 'Kennedy', 'Ivy', 'Ariana', 'Aaliyah', 'Cora', 'Madelyn', 'Alice', 'Kinsley', 'Hailey', 'Gabriella', 'Allison', 'Gianna', 'Serenity', 'Samantha', 'Sarah', 'Autumn', 'Quinn', 'Eva', 'Piper', 'Sophie', 'Sadie', 'Delilah', 'Josephine', 'Nevaeh', 'Adeline', 'Arya', 'Emery', 'Lydia', 'Clara', 'Vivian', 'Madeline', 'Peyton', 'Julia', 'Rylee', 'Brielle', 'Reagan', 'Natalia', 'Jade', 'Athena', 'Maria', 'Leilani', 'Everleigh', 'Liliana', 'Melanie', 'Mackenzie', 'Hadley', 'Raelynn', 'Kaylee', 'Rose', 'Arianna', 'Isabelle', 'Melody', 'Eliza', 'Lyla', 'Katherine', 'Aubree', 'Adalynn', 'Kylie', 'Faith', 'Mary', 'Margaret', 'Ximena', 'Iris', 'Alexandra', 'Jasmine', 'Charlie', 'Amaya', 'Taylor', 'Isabel', 'Ashley', 'Khloe', 'Ryleigh', 'Alexa', 'Amara', 'Valeria', 'Andrea', 'Parker', 'Norah', 'Eden', 'Elliana', 'Brianna', 'Emersyn', 'Valerie', 'Anastasia', 'Eloise', 'Emerson', 'Cecilia', 'Remi', 'Josie', 'Alina', 'Reese', 'Bailey', 'Lucia', 'Adalyn', 'Molly', 'Ayla', 'Sara', 'Daisy', 'London', 'Jordyn', 'Esther', 'Genevieve', 'Harmony', 'Annabelle', 'Alyssa', 'Ariel', 'Aliyah', 'Londyn', 'Juliana', 'Morgan', 'Summer', 'Juliette', 'Trinity', 'Callie', 'Sienna', 'Blakely', 'Alaia', 'Kayla', 'Teagan', 'Alaina', 'Brynlee', 'Finley', 'Catalina', 'Sloane', 'Rachel', 'Lilly', 'Ember', 'Kimberly', 'Juniper', 'Sydney', 'Arabella', 'Gemma', 'Jocelyn', 'Freya', 'June', 'Lauren', 'Amy', 'Presley', 'Georgia', 'Journee', 'Elise', 'Rosalie', 'Ada', 'Laila', 'Brooke', 'Diana', 'Olive', 'River', 'Payton', 'Ariella', 'Daniela', 'Raegan', 'Alayna', 'Gracie', 'Mya', 'Blake', 'Noelle', 'Ana', 'Leila', 'Paige', 'Lila', 'Nicole', 'Rowan', 'Hope', 'Ruth', 'Alana', 'Selena', 'Marley', 'Kamila', 'Alexis', 'Mckenzie', 'Zara', 'Millie', 'Magnolia', 'Kali', 'Kehlani', 'Catherine', 'Maeve', 'Adelyn', 'Sawyer', 'Elsie', 'Lola', 'Jayla', 'Adriana', 'Journey', 'Vera', 'Aspen', 'Joanna', 'Alivia', 'Angela', 'Dakota', 'Camille', 'Nyla', 'Tessa', 'Brooklynn', 'Malia', 'Makayla', 'Rebecca', 'Fiona', 'Mariana', 'Lena', 'Julianna', 'Vanessa', 'Juliet', 'Camilla', 'Kendall', 'Harley', 'Cali', 'Evangeline', 'Mariah', 'Jane', 'Zuri', 'Elaina', 'Sage', 'Amira', 'Adaline', 'Lia', 'Charlee', 'Delaney', 'Lilah', 'Miriam', 'Angelina', 'Mckenna', 'Aniyah', 'Phoebe', 'Michelle', 'Thea', 'Hayden', 'Maggie', 'Lucille', 'Amiyah', 'Annie', 'Alexandria', 'Myla', 'Vivienne', 'Kiara', 'Alani', 'Margot', 'Adelaide', 'Briella', 'Brynn', 'Saylor', 'Destiny', 'Amari', 'Evelynn', 'Haven', 'Phoenix', 'Izabella', 'Kaia', 'Lilliana', 'Harlow', 'Alessandra', 'Madilyn', 'Nina', 'Logan', 'Adelynn', 'Amina', 'Kate', 'Fatima', 'Samara', 'Winter', 'Giselle', 'Evie', 'Arielle', 'Jessica', 'Talia', 'Leia', 'Gabriela', 'Gracelyn', 'Lexi', 'Laura', 'Makenzie', 'Melissa', 'Royalty', 'Rylie', 'Raelyn', 'Gabrielle', 'Paris', 'Daleyza', 'Joy', 'Maisie', 'Oakley', 'Ariyah', 'Kailani', 'Alayah', 'Stephanie', 'Amora', 'Willa', 'Gracelynn', 'Elle', 'Keira', 'Tatum', 'Veronica', 'Milani', 'Felicity', 'Paislee', 'Allie', 'Nylah', 'Ariah', 'Cassidy', 'Lyric', 'Madeleine', 'Miracle', 'Gwendolyn', 'Octavia', 'Dahlia', 'Heidi', 'Celeste', 'Remington', 'Makenna', 'Everlee', 'Scarlet', 'Esmeralda', 'Maci', 'Lainey', 'Jacqueline', 'Kira', 'Lana', 'Brinley', 'Demi', 'Ophelia', 'Lennon', 'Reign', 'Bristol', 'Sabrina', 'Alaya', 'Jennifer', 'Kenzie', 'Angel', 'Luciana', 'Anaya', 'Hallie', 'Ryan', 'Camryn', 'Kinley', 'Daniella', 'Lilith', 'Blair', 'Amanda', 'Collins', 'Jordan', 'Maliyah', 'Rosemary', 'Cataleya', 'Kaylani', 'Gia', 'Alison', 'Leighton', 'Nadia', 'Sutton', 'Carolina', 'Skye', 'Alicia', 'Regina', 'Viviana', 'Yaretzi', 'Heaven', 'Serena', 'Raven', 'Emely', 'Carmen', 'Wren', 'Helen', 'Charleigh', 'Danielle', 'Daphne', 'Esme', 'Nayeli', 'Maddison', 'Sarai', 'Dylan', 'Frances', 'Elisa', 'Mabel', 'Skyler', 'Jenna', 'Emelia', 'Kaitlyn', 'Miranda', 'Marlee', 'Matilda', 'Selah', 'Jolene', 'Wynter', 'Hattie', 'Bianca', 'Haley', 'Lorelei', 'Mira', 'Braelynn', 'Annalise', 'Madelynn', 'Katie', 'Palmer', 'Aylin', 'Elliott', 'Kyla', 'Rory', 'Avianna', 'Liana', 'Shiloh', 'Kalani', 'Jada', 'Kelsey', 'Elianna', 'Jimena', 'Kora', 'Kamryn', 'Ainsley', 'Averie', 'Kensley', 'Helena', 'Holly', 'Emory', 'Macie', 'Amber', 'Zariah', 'Erin', 'Eve', 'Kathryn', 'Renata', 'Kayleigh', 'Emmy', 'Celine', 'Francesca', 'Fernanda', 'April', 'Shelby', 'Poppy', 'Colette', 'Meadow', 'Nia', 'Sierra', 'Cheyenne', 'Edith', 'Oaklynn', 'Kennedi', 'Abby', 'Danna', 'Jazlyn', 'Alessia', 'Mikayla', 'Alondra', 'Addilyn', 'Leona', 'Mckinley', 'Carter', 'Maren', 'Sylvia', 'Alejandra', 'Ariya', 'Astrid', 'Adrianna', 'Charli', 'Imani', 'Maryam', 'Christina', 'Stevie', 'Maia', 'Adelina', 'Dream', 'Aisha', 'Alanna', 'Itzel', 'Azalea', 'Katelyn', 'Kylee', 'Leslie', 'Madilynn', 'Myra', 'Virginia', 'Remy', 'Hanna', 'Aleah', 'Jaliyah', 'Antonella', 'Aviana', 'Cameron', 'Chelsea', 'Cecelia', 'Alia', 'Mae', 'Cadence', 'Emberly', 'Charley', 'Janelle', 'Mallory', 'Kaliyah', 'Elaine', 'Gloria', 'Jayleen', 'Lorelai', 'Malaysia', 'Bethany', 'Briana', 'Beatrice', 'Dorothy', 'Rosie', 'Jemma', 'Noa', 'Carly', 'Mariam', 'Anne', 'Karina', 'Emmalyn', 'Ivory', 'Ivanna', 'Jamie', 'Kara', 'Aitana', 'Jayda', 'Justice', 'Meredith', 'Briar', 'Skyla', 'Khaleesi', 'Dayana', 'Julieta', 'Katalina', 'Kendra', 'Oaklyn', 'Ashlyn', 'Armani', 'Jazmin', 'Kyra', 'Angelica', 'Zahra', 'Dallas', 'Johanna', 'Elliot', 'Macy', 'Monroe', 'Kimber', 'Henley', 'Ari', 'Karsyn', 'Lyanna', 'Lilian', 'Amalia', 'Nola', 'Dior', 'Aleena', 'Megan', 'Michaela', 'Amirah', 'Cassandra', 'Melany', 'Legacy', 'Reyna', 'Alma', 'Emmie', 'Melina', 'Siena', 'Priscilla', 'Ashlynn', 'Savanna', 'Sloan', 'Tiana', 'Aubrie', 'Coraline', 'Reina', 'Allyson', 'Kaydence', 'Sasha', 'Julie', 'Alexia', 'Irene', 'Marilyn', 'Greta', 'Braelyn', 'Emerie', 'Lylah', 'Nalani', 'Monica', 'Aileen', 'Lauryn', 'Anahi', 'Aurelia', 'Kassidy', 'Rayna', 'Romina', 'Lillie', 'Marie', 'Rosa', 'Saige', 'Bonnie', 'Kelly', 'Xiomara', 'Annabella', 'Avah', 'Lacey', 'Anya', 'Liberty', 'Karen', 'Mercy', 'Zelda', 'Baylee', 'Chaya', 'Kenna', 'Roselyn', 'Liv', 'Mara', 'Ensley', 'Malani', 'Malaya', 'Hadassah', 'Lyra', 'Adley', 'Galilea', 'Jaylah', 'Karla', 'Nala', 'Opal', 'Aliza', 'Milena', 'Ailani', 'Louisa', 'Mina', 'Kairi', 'Clementine', 'Louise', 'Maleah', 'Janiyah', 'Marina', 'Anika', 'Julissa', 'Bailee', 'Hayley', 'Jessie', 'Laney', 'Eileen', 'Faye', 'Kynlee', 'Tiffany', 'Lara', 'Angie', 'Joelle', 'Rhea', 'Calliope', 'Jazmine', 'Amani', 'Haylee', 'Aliana', 'Leyla', 'Jolie', 'Kinslee', 'Ryann', 'Simone', 'Milan', 'Lennox', 'Treasure', 'Alora', 'Ellis', 'Rebekah', 'Mikaela', 'Lina', 'Harmoni', 'Yareli', 'Giuliana', 'Lea', 'Harlee', 'Elyse', 'Frida', 'Blaire', 'Aya', 'Laurel', 'Meghan', 'Pearl', 'Zaylee', 'Alena', 'Holland', 'Bria', 'Rayne', 'Bridget', 'Zariyah', 'Kori', 'Frankie', 'Clarissa', 'Brylee', 'Davina', 'Rivka', 'Cynthia', 'Zaria', 'Madalyn', 'Paula', 'Salem', 'Amelie', 'Madisyn', 'Vienna', 'Haisley', 'Ainhoa', 'Journi', 'Karter', 'Oaklee', 'Livia', 'Miley', 'Adele', 'Amaia', 'Yara', 'Averi', 'Emmeline', 'Kyleigh', 'Princess', 'Penny', 'Sariyah', 'Amayah', 'Crystal', 'Keyla', 'Lilyana', 'Linda', 'Aniya', 'Marianna', 'Alaiya', 'Noemi', 'Chanel', 'Estella', 'Isabela', 'Jillian', 'Kallie', 'Ellianna', 'Elsa', 'Itzayana', 'Zora', 'Estelle', 'Chana', 'Raina', 'Royal', 'Sunny', 'Estrella', 'Martha', 'Ellen', 'Kailey', 'Maxine', 'Clare', 'Teresa', 'Annika', 'Kamilah', 'Azariah', 'Della', 'Addyson', 'Kai', 'Lilianna', 'Tinsley', 'Yaritza', 'Navy', 'Winnie', 'Andi', 'Kamiyah', 'Waverly', 'Sky', 'Amaris', 'Ramona', 'Saoirse', 'Hana', 'Judith', 'Halle', 'Laylah', 'Novalee', 'Jaycee', 'Zaniyah', 'Alianna', 'Paulina', 'Jayde', 'Thalia', 'Giovanna', 'Gwen', 'Iliana', 'Elora', 'Ezra', 'Kaylie', 'Braylee', 'Mavis', 'Ellison', 'Margo', 'Mylah', 'Paisleigh', 'Analia', 'August', 'Brittany', 'Kaisley', 'Belen', 'Promise', 'Amiya', 'Dalary', 'Veda', 'Alisson', 'Keilani', 'Oakleigh', 'Guadalupe', 'Leanna', 'Rosalyn', 'Selene', 'Theodora', 'Kamari', 'Anais', 'Elodie', 'Celia', 'Dani', 'Hunter', 'Indie', 'Kenia', 'Nellie', 'Belle', 'Kataleya', 'Lexie', 'Miah', 'Rylan', 'Sylvie', 'Valery', 'Addilynn', 'Dulce', 'Marissa', 'Meilani', 'Natasha', 'Jaylee', 'Kimora', 'Raquel', 'Scarlette', 'Aliya', 'Nataly', 'Whitney', 'Corinne', 'Denver', 'Nathalie', 'Kiera', 'Milana', 'Vada', 'Violeta', 'Luz', 'Addisyn', 'Casey', 'Deborah', 'Tori', 'Zainab', 'Erika', 'Jenesis', 'Avalynn', 'Nancy', 'Emmalynn', 'Hadlee', 'Heavenly', 'Aubrielle', 'Elisabeth', 'Salma', 'Adalee', 'Landry', 'Malayah', 'Novah', 'Egypt', 'Ayleen', 'Blessing', 'Elina', 'Joyce', 'Myah', 'Zoie', 'Christine', 'Jaelynn', 'Persephone', 'Chandler', 'Emmaline', 'Paloma', 'Harleigh', 'Noor', 'Paola', 'India', 'Madalynn', 'Rosalee', 'Florence', 'Maliah', 'Flora', 'Luella', 'Patricia', 'Whitley', 'Carolyn', 'Kathleen', 'Keily', 'Kiana', 'Tenley', 'Alyson', 'Barbara', 'Dana', 'Yasmin', 'Bexley', 'Micah', 'Tatiana', 'Arden', 'Aubriella', 'Lindsey', 'Emani', 'Hailee', 'Lisa', 'Sevyn', 'Fallon', 'Magdalena', 'Tinley', 'Halo', 'Lailah', 'Arlette', 'Ansley', 'Esperanza', 'Cleo', 'Aila', 'Emerald', 'Jaelyn', 'Karlee', 'Kaya', 'Ingrid', 'Jewel', 'Emilee', 'Giana', 'Paityn', 'Zola', 'Amoura', 'Renee', 'Ann', 'Berkley', 'Harriet', 'Queen', 'Sariah', 'Beatrix', 'Sandra', 'Alannah', 'Austyn', 'Freyja', 'Kaylin', 'Samira', 'Taliyah', 'Hadleigh', 'Kaiya', 'Robin', 'Luisa', 'Zendaya', 'Ariadne', 'Dixie']

names = male_names + female_names

colors = [
    "Red","Orange","Yellow","Green","Blue","Purple",
    "Tan","Turquoise","Silver","Pink","Gray",
]

emotion_adj = [
    "Accepting","Accommodating","Afraid","Aggressive","Agitated","Alarmed","Amazed",
    "Amused","Antagonistic","Anxious","Apathetic","Apprehensive","Arrogant","Bothered","Brave","Calm","Charming",
    "Cheerful","Competitive","Confident","Conscientious","Conservative","Creative","Curious",
    "Cynical","Distracted","Distraught","Distressed","Downcast",
    "Earnest","Gloomy","Grouchy","Guilty","Heroic","Hopeful",
    "Hostile","Humble","Jovial","Joyful","Jumpy","Mysterious","Opinionated",
    "Panicky","Passionate","Patient","Quarrelsome","Rational","Reasonable",
    "Sad","Safe","Scared","Scornful","Selfish",
    "Thoughtful","Tolerant","Tranquil","Treacherous","Welcoming","Witty","Zealous","Zany",
    "Supportive","Sardonic","Secretive","Bitter",
]

nouns = [
    "actor","artist","butler","crook","director",
    "expert","fisherman","judge","juror","painter","musician",
    "policeman","fireman","professor","sheriff","soldier","student",
    "philosopher","teacher","tourist","lawyer","physician","engineer",
    "veterinarian","dentist","accountant","technician","electrician",
    "psychologist","physicist","plumber","waiter","mechanic","cook",
    "librarian","hairdresser","economist","bartender","cashier","surgeon",
    "pilot","butcher","optician","athlete","cleaner",
    "actuary","sailor","therapist","secret_agent","animal_breeder","air_traffic_controller",
    "athropologist","animal_trainer","allergist","real_estate_agent","archeologist",
    "astronomer","athletic_trainer","audiologist","auditor","bailiff",
    "baker","barber","clerk","cartographer","chiropractor","dancer","epidemiologist",
    "farmer","floral_designer","forester","truck_driver","jeweler","interior_designer",
    "machinist","mathematician","secretary","photographer","radio_announcer","roofer",
    "paver","taxi_driver","historian","poet","stunt_performer","monologist","publisher",
    "scribe","blogger","copy_editor","ceo","ticket_controller","station_master","surveyor",
    "driller", "scholar", "quant", "cfo" , "cto", "cio", "computer_scientist", "prisoner",
    "guest", "visitor", "helper", "breadwinner", "host", "ghost", "playmaker", "scorer",
    "settler", "reacher", "cynic", "witch", "captain", "buisness_analyst", "data_scientist",
    "trader", "principal", "ballerina", "footballer", "cricketer", "tennis_player", "lecturer",
    "patient", "ai_scientist", "philosopher", "cyclist", "chess_player", "stratergist",
    "scientist", "parent", "fbi_agent", "defender" , "attacker", "warlord", "nlp_engineer",
    "grandmaster", "master", "king", "queen", "knight", "prince", "princess", "baby", "adult",
    "advisor", "wrestler", "fighter", "boxer", "bee_keeper", "musian", "dj_artist", "violinist",
    "conductor", "gymnast"
]

count_furniture = [
    "chair","table","desk","stool","couch","bookcase",
    "bed","mattress","dresser","futon","nightstand","storage_container",
    "hammock","billiard_table","piano","chess_board","door",
]


count_animals = [
    "aardvark","dog","alpaca","armadillo","anteater","penguin",
    "ant","bear","bonobo","beaver","bird","owl","butterfly",
    "buffalo","bumblebee","frog","whale","bison","badger","baboon",
    "rhinoceros","camel","cat","chicken","cheetah","cockatoo","cow","crab",
    "catepillar","chimpanzee","loon","spider","crocodile","coyote","chincilla",
    "duck","deer","dolphin","dingo","donkey","eel","elephant","emu","gorilla","falcon",
    "fox","ferret","gerbil","grasshopper","gopher","goat","hyena","horse","hippopotamus",
    "jaguar","kangaroo","lemur","lion","lynx","lizard","marmot","mink","muskrat","mouse",
    "macaw","moose","newt","ostrich","otter","pig","puffin","puma","pelican","peacock",
    "rabbit","snake","reindeer","raccoon","rat","sheep","vulture","wombat","wolf","warthog",
    "walrus","weasel","boar","zebra","seal",
]

verbs = ["like", "admire", "pet", "make", "break", "hit", "eat", "kill", "fight", "steal", "touch",
         "approve", "defend", "replace", "chase", "hunt", "dislike", "recognize", "understand", "feel",
         "love", "hate", "impress", "know", "notice", "perceive", "see", "remember", "surprise", "prefer",
         "draw", "accuse", "adore", "advise", "appreciate", "approach", "astonish", "need", "call", "believe",
         "follow", "serve", "consult", "convince", "criticize", "desire", "doubt", "encourage", "examine",
         "feed", "forgive", "hug", "investigate", "kiss", "mention", "owe", "persuade", "propose", "promise",
         "punch", "shoot", "threaten", "tolerate", "warn"]




class Anaphora:

    def __init__(self):
      pass


    def template_anaphora(self, template_name):
      templates = {
          "2q_n_v_n_v_si_si": "{} {} {} {} {} who {} {}",
          "2q_n_v_n_v_si_pl": "{} {} {} {} {} who {} {}",
          "2q_n_v_n_v_pl_si": "{} {} {} {} {} who {} {}",
          "2q_n_v_n_v_pl_pl": "{} {} {} {} {} who {} {}",
          "2q_n_v_n_v_neg_si_si": "{} {} {} {} {} who does not {} {}",
          "2q_n_v_n_v_neg_si_pl": "{} {} {} {} {} who do not {} {}",
          "2q_n_v_n_v_neg_pl_si": "{} {} {} {} {} who does not {} {}",
          "2q_n_v_n_v_neg_pl_pl": "{} {} {} {} {} who do not {} {}",
          "2q_n_v_neg_n_v_si_si": "{} {} does not {} {} {} who {} {}",
          "2q_n_v_neg_n_v_pl_si": "{} {} do not {} {} {} who {} {}",
          "2q_n_v_neg_n_v_si_pl": "{} {} does not {} {} {} who {} {}",
          "2q_n_v_neg_n_v_pl_pl": "{} {} do not {} {} {} who {} {}",
          "2q_n_v_neg_n_v_neg_si_si": "{} {} does not {} {} {} who does not {} {}",
          "2q_n_v_neg_n_v_neg_si_pl": "{} {} does not {} {} {} who do not {} {}",
          "2q_n_v_neg_n_v_neg_pl_si": "{} {} do not {} {} {} who does not {} {}",
          "2q_n_v_neg_n_v_neg_pl_pl": "{} {} do not {} {} {} who do not {} {}",
          "2q_n_v_n_neg_v_si_si": "{} {} {} {} non-{} who {} {}",
          "2q_n_v_n_neg_v_si_pl": "{} {} {} {} non-{} who {} {}",
          "2q_n_v_n_neg_v_pl_si": "{} {} {} {} non-{} who {} {}",
          "2q_n_v_n_neg_v_pl_pl": "{} {} {} {} non-{} who {} {}",
          "2q_n_v_n_neg_v_neg_si_si": "{} {} {} {} non-{} who does not {} {}",
          "2q_n_v_n_neg_v_neg_si_pl": "{} {} {} {} non-{} who do not {} {}",
          "2q_n_v_n_neg_v_neg_pl_si": "{} {} {} {} non-{} who does not {} {}",
          "2q_n_v_n_neg_v_neg_pl_pl": "{} {} {} {} non-{} who do not {} {}",
          "2q_n_v_neg_n_neg_v_si_si": "{} {} does not {} {} non-{} who {} {}",
          "2q_n_v_neg_n_neg_v_pl_si": "{} {} do not {} {} non-{} who {} {}",
          "2q_n_v_neg_n_neg_v_si_pl": "{} {} does not {} {} non-{} who {} {}",
          "2q_n_v_neg_n_neg_v_pl_pl": "{} {} do not {} {} non-{} who {} {}",
          "2q_n_v_neg_n_neg_v_neg_si_si": "{} {} does not {} {} non-{} who does not {} {}",
          "2q_n_v_neg_n_neg_v_neg_si_pl": "{} {} does not {} {} non-{} who do not {} {}",
          "2q_n_v_neg_n_neg_v_neg_pl_si": "{} {} do not {} {} non-{} who does not {} {}",
          "2q_n_v_neg_n_neg_v_neg_pl_pl": "{} {} do not {} {} non-{} who do not {} {}",
          "2q_n_neg_v_n_v_si_si": "{} non-{} {} {} {} who {} {}",
          "2q_n_neg_v_n_v_si_pl": "{} non-{} {} {} {} who {} {}",
          "2q_n_neg_v_n_v_pl_si": "{} non-{} {} {} {} who {} {}",
          "2q_n_neg_v_n_v_pl_pl": "{} non-{} {} {} {} who {} {}",
          "2q_n_neg_v_n_v_neg_si_si": "{} non-{} {} {} {} who does not {} {}",
          "2q_n_neg_v_n_v_neg_si_pl": "{} non-{} {} {} {} who do not {} {}",
          "2q_n_neg_v_n_v_neg_pl_si": "{} non-{} {} {} {} who does not {} {}",
          "2q_n_neg_v_n_v_neg_pl_pl": "{} non-{} {} {} {} who do not {} {}",
          "2q_n_neg_v_neg_n_v_si_si": "{} non-{} does not {} {} {} who {} {}",
          "2q_n_neg_v_neg_n_v_si_pl": "{} non-{} does not {} {} {} who {} {}",
          "2q_n_neg_v_neg_n_v_pl_si": "{} non-{} do not {} {} {} who {} {}",
          "2q_n_neg_v_neg_n_v_pl_pl": "{} non-{} do not {} {} {} who {} {}",
          "2q_n_neg_v_neg_n_v_neg_si_si": "{} non-{} does not {} {} {} who does not {} {}",
          "2q_n_neg_v_neg_n_v_neg_si_pl": "{} non-{} does not {} {} {} who do not {} {}",
          "2q_n_neg_v_neg_n_v_neg_pl_si": "{} non-{} do not {} {} {} who does not {} {}",
          "2q_n_neg_v_neg_n_v_neg_pl_pl": "{} non-{} do not {} {} {} who do not {} {}",
          "2q_n_neg_v_n_neg_v_si_si": "{} non-{} {} {} non-{} who {} {}",
          "2q_n_neg_v_n_neg_v_si_pl": "{} non-{} {} {} non-{} who {} {}",
          "2q_n_neg_v_n_neg_v_pl_si": "{} non-{} {} {} non-{} who {} {}",
          "2q_n_neg_v_n_neg_v_pl_pl": "{} non-{} {} {} non-{} who {} {}",
          "2q_n_neg_v_n_neg_v_neg_si_si": "{} non-{} {} {} non-{} who does not {} {}",
          "2q_n_neg_v_n_neg_v_neg_si_pl": "{} non-{} {} {} non-{} who do not {} {}",
          "2q_n_neg_v_n_neg_v_neg_pl_si": "{} non-{} {} {} non-{} who does not {} {}",
          "2q_n_neg_v_n_neg_v_neg_pl_pl": "{} non-{} {} {} non-{} who do not {} {}",
          "2q_n_neg_v_neg_n_neg_v_si_si": "{} non-{} does not {} {} non-{} who {} {}",
          "2q_n_neg_v_neg_n_neg_v_si_pl": "{} non-{} does not {} {} non-{} who {} {}",
          "2q_n_neg_v_neg_n_neg_v_pl_si": "{} non-{} do not {} {} non-{} who {} {}",
          "2q_n_neg_v_neg_n_neg_v_pl_pl": "{} non-{} do not {} {} non-{} who {} {}",
          "2q_n_neg_v_neg_n_neg_v_neg_si_si": "{} non-{} does not {} {} non-{} who does not {} {}",
          "2q_n_neg_v_neg_n_neg_v_neg_si_pl": "{} non-{} does not {} {} non-{} who do not {} {}",
          "2q_n_neg_v_neg_n_neg_v_neg_pl_si": "{} non-{} do not {} {} non-{} who does not {} {}",
          "2q_n_neg_v_neg_n_neg_v_neg_pl_pl": "{} non-{} do not {} {} non-{} who do not {} {}",
          "propn_v_n_v_si": "{} {} {} {} who {} {}",
          "propn_v_n_v_pl": "{} {} {} {} who {} {}",
          "propn_v_n_v_neg_si": "{} {} {} {} who does not {} {}",
          "propn_v_n_v_neg_pl": "{} {} {} {} who do not {} {}",
          "propn_v_neg_n_v_si": "{} does not {} {} {} who {} {}",
          "propn_v_neg_n_v_pl": "{} does not {} {} {} who {} {}",
          "propn_v_neg_n_v_neg_si": "{} does not {} {} {} who does not {} {}",
          "propn_v_neg_n_v_neg_pl": "{} does not {} {} {} who do not {} {}",
          "propn_v_n_neg_v_si": "{} {} {} non-{} who {} {}",
          "propn_v_n_neg_v_pl": "{} {} {} non-{} who {} {}",
          "propn_v_n_neg_v_neg_si": "{} {} {} non-{} who does not {} {}",
          "propn_v_n_neg_v_neg_pl": "{} {} {} non-{} who do not {} {}",
          "propn_v_neg_n_neg_v_si": "{} does not {} {} non-{} who {} {}",
          "propn_v_neg_n_neg_v_pl": "{} does not {} {} non-{} who {} {}",
          "propn_v_neg_n_neg_v_neg_si": "{} does not {} {} non-{} who does not {} {}",
          "propn_v_neg_n_neg_v_neg_pl": "{} does not {} {} non-{} who do not {} {}",
      }

      return templates[template_name]


    def select_det(self, quantifier):
      det = None
      if quantifier == "all":
        det = random.choice(["all", "every"])
      elif quantifier == "exists":
        det = random.choice(["some", "a"])
      return det

    def natural_language_sentence_generation(self, quantifiers, variables, verb_functions, negations, type, male_name = False):
      dets = None

      if type == "2_quantifiers":
        dets = [self.select_det(quantifiers[0]), self.select_det(quantifiers[1])]
        template_id = "2q_n_"
        if negations[variables[0]] == True:
          template_id += "neg_"
        template_id += "v_"
        if negations[verb_functions[1]] == True:
          if quantifiers[0] == "all":
            dets[0] = "no"
            if quantifiers[1] == "all":
              dets[1] = "any"
            else :
              dets[1] = "every"
          elif (quantifiers[0] == "exists") and (quantifiers[1] == "exists"):
            dets[1] = "no"
          else :
            template_id += "neg_"
        template_id += "n_"
        if negations[variables[1]] == True:
          template_id += "neg_"
        template_id += "v_"
        if negations[verb_functions[0]] == True:
          template_id += "neg_"

        if dets[0] in ["all", "some"]:
          template_id += "pl_"
          pronoun = "them"
        else :
          template_id += "si_"
          pronoun = random.choice(["him", "her"])

        if dets[1] in ["all", "some"]:
          template_id += "pl"
        else :
          template_id += "si"

        return self.template_anaphora(template_id).format(dets[0], variables[0], verb_functions[1], dets[1], variables[1], verb_functions[0], pronoun)

      else :
        dets = [self.select_det(quantifiers[0])]
        template_id = "propn_v_"
        if negations[verb_functions[1]] == True :
          if quantifiers[0] == "exists":
            dets[0] = "no"
          else :
            template_id += "neg_"
        template_id += "n_"
        if negations[variables[1]] == True :
          template_id += "neg_"
        template_id += "v_"
        if negations[verb_functions[0]] == True :
          template_id += "neg_"

        template_id += "pl" if dets[0] in ["all", "some"] else "si"

        pronoun = "him" if male_name else "her"

        return self.template_anaphora(template_id).format(variables[0], verb_functions[1], dets[0], variables[1], verb_functions[0], pronoun)



    def anaphora_generate_logic_str(self, quantifiers, variables, verb_functions, negations, type):

      variables = ["-"+x if negations[x] else x for x in variables]
      verb_functions = ["-"+x if negations[x] else x for x in verb_functions]


      if type == "2_quantifiers":
        if quantifiers == ["all", "all"]:
          return "all x.({}(x) -> all y.({}(y) & {}(y,x) -> {}(x,y)))".format(variables[0], variables[1], verb_functions[0], verb_functions[1])
        elif quantifiers == ["all", "exists"]:
          return "all x.({}(x) -> exists y.({}(y) & {}(y,x) & {}(x,y)))".format(variables[0], variables[1], verb_functions[0], verb_functions[1])
        elif quantifiers == ["exists", "all"]:
          return "exists x.({}(x) & all y.({}(y) & {}(y,x) -> {}(x,y)))".format(variables[0], variables[1], verb_functions[0], verb_functions[1])
        elif quantifiers == ["exists", "exists"]:
          return "exists x.({}(x) & exists y.({}(y) & {}(y,x) & {}(x,y)))".format(variables[0], variables[1], verb_functions[0], verb_functions[1])
      else :
        if quantifiers == ["all"]:
          return "all x.({}(x) & {}(x, {}) -> {}({}, x))".format(variables[1], verb_functions[0] ,variables[0], verb_functions[1], variables[0])
        else :
          return "exists x.({}(x) & {}(x, {}) & {}({}, x))".format(variables[1], verb_functions[0] ,variables[0], verb_functions[1], variables[0])


    def generate_sentence_anaphora(self, nouns, domain, verbs, prob = 0.85):

      verb_functions = random.sample(verbs, 2)

      male_name = False

      negations = None

      if random.uniform(0,1) < prob :
        noun_functions = random.sample(nouns, 2)
        type = "2_quantifiers"
        quantifiers = [random.choice(["all", "exists"]), random.choice(["all", "exists"])]
        variables = random.sample(nouns, 2)


        negations = {variables[0] : random.choice([True, False]),
                  variables[1] : random.choice([True, False]),
                  verb_functions[0] : random.choice([True, False]),
                  verb_functions[1] : random.choice([True, False])}

      else :
        quantifiers = [random.choice(["all", "exists"])]

        type = "PropN"

        variables = [random.choice(domain), random.choice(nouns)]
        negations = {variables[0] : False,
                    variables[1] : random.choice([True, False]),
                    verb_functions[0] : random.choice([True, False]),
                    verb_functions[1] : random.choice([True, False])}


      male_name = False if variables[0] in female_names else True


      logic = self.anaphora_generate_logic_str(quantifiers, variables, verb_functions, negations, type)
      sentence = self.natural_language_sentence_generation(quantifiers, variables, verb_functions, negations, type, male_name)

      return logic, sentence


