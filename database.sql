create database mycare;
use database mycare;

create table users(
  id int auto_increment primary key,
  username varchar(100) not null,
  type varchar(20) not null,
  password varchar(25) unique not null);

create table medicine(
  mid int auto_increment primary key,
  mname varchar(50) not null,
  manufacture date,
  expiry date);

create table patient(
  pid int auto_increment primary key.
  pname varchar(100) not null,
  status varchar(50)not null,
  mid int,
  dosage int not null,
  frequency int not null,
  foreign key (mid) references medicine(mid));

create table logs(
  srno int auto_increment primary key,
  pid int,
  mid int,
  timestamp timestamp deefault current_timestamp,
  status varchar(10),
  foreign key(mid) references medicine(mid),
  foreign key(pid) references patient(pid));
  
