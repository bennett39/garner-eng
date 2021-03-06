# garner-eng

![Screenshot of home page](http://www.garner-eng.com/wp-content/uploads/2018/11/Screenshot-2018-11-27-at-20.31.15.png)

This web app allows an engineering firm to track their projects, clients, and construction sites with a custom-developed dashboard and CRM-like editing.

It's a Django web application that uses Bootstrap for style. It can deploy to any server and database setup, including cloud providers. I've deployed it to Google App Engine with a MySQL Cloud instance.

Current features:
- Detailed models for projects, clients, contacts, sites, and daily field reports
- User authentication using Django's auth

Next steps under development:
- Add search functionality
- Add data visualization to the dashboard
- Implement AJAX page editing to avoid page reloading
