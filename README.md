# Sentry -> Telegram
Webhook for Sentry which allow send alerts to Telegram

#### How to use
1. Clone repo
2. Create .env file with TOKEN=*botfathertoken* and CHATID=*yourchatid*
3. Build docker image
4. Run docker run -d -p 5000:5000 *image*
5. Add to Sentry project webhook integration with your domain or IP.