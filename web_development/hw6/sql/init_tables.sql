create sequence if not exists user_seq start with 1 increment by 1 cache 25;
create sequence if not exists site_acct_data_seq start 1 increment by 1 cache 25;

create type login_type as enum ('apple', 'google', 'facebook', 'email');

create table if not exists users
(
    user_id  int primary key default nextval('user_seq'),
    username varchar(40) unique not null,
    email    varchar(60) unique not null,
    password varchar(24)        not null
);

create table if not exists site_acct_data
(
    rec_id       int primary key default nextval('site_acct_data_seq'),
    usr_id       int          not null,
    site_url     varchar(100) not null,
    account_type login_type   not null,
    site_login   varchar(100) not null,
    site_password varchar(100),
    foreign key (usr_id) references users (user_id)
);

create unique index site_acct_data_unq_idx on site_acct_data (usr_id, site_url, account_type);
