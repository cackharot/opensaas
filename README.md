opensaas
========

An open source multi-tenant SAAS service which eases the SAAS application development by providing the foundational/common features and drives the app development to focus on the core business functionality instead of these.

Background and motivation: Lately most of the web application are developed in SAAS multi-tenant model with maturing cloud and web technologies. To build these saas application one needs to build various underlying foundational features in addition to their core unique business functionality. These foundational features which seems - no are common to all the saas application. This project aims to deliver those and enables you to develop your bussiness app more rapidly and effectively.

Objective:
==========
To provide the foundational/common features required by the saas applications.

Feature list:
=============
Subscription Management
Tenant Management
User Management
Security Management
Authentication/Authorization
Activity Stream
Scaling

Architecture
============
The above features will be available as REST API which can be used in your business application. There is also Web application available to manage the above features like onboarding new customer, creating subscription plans, managing security etc, we call it as "saasportal".

This enables that your app can be developed in any technology.

opensaas technology:
====================
Python 3.0
Postgres SQL
MongoDb
Pyramid Web Framework

Milestone 0.1:
==============
Basic setup, tenant, user, security management

Milestone 0.2:
==============
Subscription management

Milestone 0.3:
==============
Activity stream and scaling

