from pathlib import Path
import html, re

DEST = Path('.')
TARGET = 'https://lotit.net/'

items = [
('amazon-gift-card','Amazon Gift Card Rewards','amazon gift card, Amazon gift card reward, gift card offers',200,'classic'),
('amazon-gift-card-reward','Amazon Gift Card Reward Offers','Amazon gift card reward, online gift card reward, reward offers',100,'guide'),
('free-amazon-gift-card','Free Amazon Gift Card Offers','free Amazon gift card, free gift card offers, gift card promotion',50,'minimal'),
('amazon-gift-card-promotion','Amazon Gift Card Promotion Guide','Amazon gift card promotion, gift card promotion, online rewards',150,'guide'),
('amazon-reward-card','Amazon Reward Card Opportunities','Amazon reward card, gift card rewards, reward opportunities',100,'dark'),
('gift-card-rewards','Gift Card Rewards Online','gift card rewards, online rewards, gift card offers',200,'classic'),
('gift-card-offers','Gift Card Offers & Promotions','gift card offers, gift card promotion, reward offers',75,'minimal'),
('free-gift-card','Free Gift Card Offers Guide','free gift card, free gift card offers, online gift cards',100,'guide'),
('gift-card-giveaway','Gift Card Giveaway Guide','gift card giveaway, gift card rewards, promotional gifts',150,'bright'),
('gift-card-bonus','Gift Card Bonus Opportunities','gift card bonus, reward bonus, gift card offers',50,'minimal'),
('online-gift-card','Online Gift Card Rewards','online gift card, digital gift card, reward offers',200,'classic'),
('gift-card-deals','Gift Card Deals & Reward Offers','gift card deals, gift card rewards, promotional offers',100,'guide'),
('gift-card-promo','Gift Card Promo Opportunities','gift card promo, gift card promotion, reward opportunities',150,'bright'),
('reward-card-offers','Reward Card Offers Online','reward card, reward card offers, online rewards',75,'dark'),
('shopping-gift-card','Shopping Gift Card Rewards','shopping gift card, gift card reward, shopping rewards',100,'classic'),
('online-rewards-gift-card','Online Rewards & Gift Cards','online rewards, gift card rewards, reward offers',200,'guide'),
('instant-gift-card','Gift Card Reward Opportunities','gift card reward opportunities, digital rewards, gift cards',50,'minimal'),
('gift-card-task','Gift Card Offers After a Qualifying Task','gift card task, qualifying task, gift card reward',100,'bright'),
('easy-gift-card-reward','Easy Gift Card Reward Guide','easy gift card reward, reward offers, gift card promotion',150,'classic'),
('gift-card-survey','Gift Card Survey Reward Guide','gift card survey, survey rewards, gift card offers',75,'guide'),
('gift-card-quiz','Gift Card Quiz & Reward Guide','gift card quiz, quiz rewards, gift card promotion',100,'dark'),
('gift-card-activity','Gift Card Activity Rewards','gift card activity, reward activities, gift card offers',200,'classic'),
('reward-offer-guide','Reward Offer Guide','reward offer, reward offers online, gift card rewards',50,'minimal'),
('gift-card-eligibility','Gift Card Eligibility Guide','gift card eligibility, reward eligibility, gift card offers',100,'guide'),
('gift-card-requirements','Gift Card Offer Requirements','gift card requirements, qualifying offers, gift card rewards',150,'classic'),
('gift-card-how-it-works','How Gift Card Rewards Work','how gift card rewards work, gift card offers, online rewards',75,'bright'),
('gift-card-tips','Gift Card Reward Tips','gift card tips, reward offers, gift card promotion',100,'minimal'),
('gift-card-guide','Complete Gift Card Reward Guide','gift card guide, gift card rewards, free gift cards',200,'classic'),
('reward-card-guide','Reward Card Guide','reward card guide, reward offers, digital gift cards',150,'guide'),
('gift-card-value','$50 to $200 Gift Card Rewards','50 dollar gift card, 100 dollar gift card, 200 dollar gift card',200,'dark'),
('50-dollar-gift-card','$50 Gift Card Reward Guide','$50 gift card, 50 dollar gift card, gift card reward',50,'bright'),
('75-dollar-gift-card','$75 Gift Card Reward Guide','$75 gift card, gift card offers, reward card',75,'minimal'),
('100-dollar-gift-card','$100 Gift Card Reward Guide','$100 gift card, 100 dollar gift card, reward offers',100,'classic'),
('150-dollar-gift-card','$150 Gift Card Reward Guide','$150 gift card, gift card promotion, reward offers',150,'guide'),
('200-dollar-gift-card','$200 Gift Card Reward Guide','$200 gift card, 200 dollar gift card, gift card reward',200,'dark'),
('gift-card-200-reward','$200 Gift Card Reward Opportunities','$200 reward, gift card rewards, online promotions',200,'bright'),
('gift-card-100-reward','$100 Gift Card Reward Opportunities','$100 reward, gift card offers, online rewards',100,'classic'),
('gift-card-50-reward','$50 Gift Card Reward Opportunities','$50 reward, gift card offers, promotional rewards',50,'minimal'),
('best-gift-card-offers','Gift Card Offer Ideas','best gift card offers, gift card rewards, reward opportunities',100,'guide'),
('gift-card-online-offers','Online Gift Card Offers','online gift card offers, digital rewards, gift card promotion',150,'classic'),
('digital-gift-card-reward','Digital Gift Card Reward Guide','digital gift card, digital reward, online gift card',100,'dark'),
('gift-card-reward-online','Gift Card Reward Online','gift card reward online, reward offers, digital gift cards',200,'bright'),
('gift-card-promotions','Gift Card Promotions Online','gift card promotions, promotional rewards, gift cards',75,'minimal'),
('reward-promotion','Reward Promotion Guide','reward promotion, gift card promotion, online rewards',150,'guide'),
('gift-card-incentive','Gift Card Incentive Guide','gift card incentive, promotional incentive, reward offers',50,'classic'),
('gift-card-perks','Gift Card Perks & Rewards','gift card perks, reward benefits, gift card offers',100,'bright'),
('gift-card-savings','Gift Card Rewards & Savings','gift card savings, gift card rewards, shopping rewards',200,'classic'),
('shopping-reward-card','Shopping Reward Card Guide','shopping reward card, reward cards, gift card offers',150,'dark'),
('consumer-reward-card','Consumer Reward Card Guide','consumer reward, reward card, gift card promotion',75,'guide'),
('reward-opportunities','Online Reward Opportunities','reward opportunities, online rewards, gift card offers',100,'minimal'),
('promotional-gift-card','Promotional Gift Card Guide','promotional gift card, gift card promotion, reward offers',200,'classic'),
('gift-card-campaign','Gift Card Campaign Guide','gift card campaign, reward campaign, promotional offers',150,'bright'),
('reward-campaign','Reward Campaign Opportunities','reward campaign, gift card rewards, online promotion',100,'dark'),
('gift-card-event','Gift Card Promotion Events','gift card event, promotional rewards, gift card offers',50,'minimal'),
('gift-card-reward-event','Gift Card Reward Events','gift card reward event, gift card promotion, rewards',75,'guide'),
('gift-card-claim-guide','Gift Card Reward Claim Guide','gift card claim, reward claim, gift card offers',100,'classic'),
('gift-card-redemption','Gift Card Redemption Guide','gift card redemption, digital gift card, reward guide',150,'dark'),
('reward-redemption','Reward Redemption Guide','reward redemption, gift card rewards, online offers',200,'bright'),
('gift-card-delivery','Gift Card Delivery Guide','gift card delivery, digital rewards, gift card offers',100,'minimal'),
('gift-card-availability','Gift Card Availability Guide','gift card availability, reward availability, gift card offers',75,'guide'),
('gift-card-access','Access Gift Card Reward Offers','gift card access, reward offers, online gift cards',150,'classic'),
('gift-card-discovery','Discover Gift Card Rewards','discover gift cards, gift card rewards, reward offers',50,'bright'),
('gift-card-finder','Gift Card Reward Finder Guide','gift card finder, gift card offers, reward opportunities',100,'dark'),
('reward-finder','Online Reward Finder','reward finder, online rewards, gift card offers',200,'classic'),
('gift-card-search','Gift Card Reward Search Guide','gift card search, gift card rewards, promotional offers',150,'guide'),
('reward-search','Reward Offer Search Guide','reward search, reward offers, gift card promotion',75,'minimal'),
('gift-card-options','Gift Card Reward Options','gift card options, reward options, online gift cards',100,'bright'),
('reward-options','Online Reward Options','reward options, online rewards, gift card offers',200,'classic'),
('gift-card-choice','Choosing a Gift Card Offer','gift card choice, gift card offers, reward options',150,'guide'),
('gift-card-checklist','Gift Card Offer Checklist','gift card checklist, offer requirements, reward guide',100,'dark'),
('reward-checklist','Reward Offer Checklist','reward checklist, gift card rewards, promotion guide',50,'minimal'),
('gift-card-faq','Gift Card Reward FAQ','gift card FAQ, gift card rewards, gift card offers',75,'classic'),
('gift-card-questions','Gift Card Reward Questions Answered','gift card questions, reward FAQ, gift card promotion',100,'bright'),
('gift-card-basics','Gift Card Reward Basics','gift card basics, reward offers, online gift cards',150,'guide'),
('reward-basics','Online Reward Basics','reward basics, gift card offers, promotional rewards',200,'dark'),
('gift-card-explained','Gift Card Rewards Explained','gift card explained, gift card rewards, online offers',100,'classic'),
('reward-explained','Reward Offers Explained','reward offers explained, gift cards, online rewards',75,'minimal'),
('gift-card-steps','Gift Card Reward Steps','gift card steps, qualifying task, reward offers',150,'bright'),
('reward-steps','Reward Offer Steps','reward steps, gift card promotion, qualifying offers',100,'guide'),
('gift-card-start','Start Exploring Gift Card Rewards','start gift card rewards, gift card offers, online promotions',50,'dark'),
('reward-start','Start Exploring Reward Offers','start reward offers, gift card rewards, promotional offers',75,'classic'),
('gift-card-opportunity','Gift Card Reward Opportunities','gift card opportunity, reward opportunities, gift cards',200,'bright'),
('reward-opportunity','Reward Opportunity Guide','reward opportunity, gift card offers, online rewards',150,'guide'),
('gift-card-promotion-guide','Gift Card Promotion Guide','gift card promotion guide, gift cards, reward offers',100,'minimal'),
('reward-promotion-guide','Reward Promotion Guide Online','reward promotion guide, gift card promotion, rewards',75,'dark'),
('gift-card-incentives','Gift Card Incentives Online','gift card incentives, reward offers, promotional gifts',150,'classic'),
('reward-incentives','Online Reward Incentives','reward incentives, gift card rewards, online offers',100,'bright'),
('gift-card-benefits','Gift Card Reward Benefits','gift card benefits, reward offers, promotional rewards',200,'guide'),
('reward-benefits','Reward Offer Benefits','reward benefits, gift card promotion, online rewards',150,'dark'),
('gift-card-ideas','Gift Card Reward Ideas','gift card ideas, reward ideas, gift card offers',75,'minimal'),
('reward-ideas','Online Reward Ideas','reward ideas, gift card rewards, promotional offers',100,'classic'),
('gift-card-promotional-offer','Promotional Gift Card Offers','promotional gift card offers, gift card reward, online promotion',200,'bright'),
('reward-promotional-offer','Promotional Reward Offers','promotional reward offers, gift cards, online rewards',150,'guide'),
('gift-card-digital','Digital Gift Card Offers','digital gift card offers, online rewards, gift card promotion',100,'dark'),
('reward-digital','Digital Reward Offers','digital rewards, gift card offers, online promotion',75,'minimal'),
('gift-card-online','Gift Card Offers Online','gift card offers online, free gift card opportunities, rewards',200,'classic'),
('reward-online','Online Reward Offers','online reward offers, gift card rewards, promotions',150,'bright'),
('gift-card-promo-guide','Gift Card Promo Guide','gift card promo guide, gift card offers, rewards',100,'guide'),
('reward-promo-guide','Reward Promo Guide','reward promo guide, gift card promotion, online rewards',50,'dark'),
('gift-card-reward-guide','Gift Card Reward Guide','gift card reward guide, Amazon gift card, gift card offers',200,'classic'),
('final-gift-card-guide','Ultimate Gift Card Reward Guide','gift card reward guide, free gift card offers, online rewards',200,'bright'),
]

styles = {
'classic': ('#ffb000','#17191c'), 'guide': ('#ffd23f','#20242a'), 'minimal': ('#f4b000','#111315'),
'dark': ('#ffb000','#0d1117'), 'bright': ('#ffc62e','#24282d')
}

for idx,(slug,title,keywords,amount,style) in enumerate(items,1):
    accent,dark = styles[style]
    phrase = keywords.split(',')[0].strip()
    extra = (idx % 4) + 2
    sections = [
        ('What this gift card reward page covers', f'This page focuses on {phrase} and related promotional opportunities. Visitors researching gift card rewards, online promotions, digital gift cards, and qualifying activities can use this guide to understand the basics before visiting an offer destination.'),
        ('How promotional gift card offers can work', 'A promotional campaign may present an activity, survey, registration, app action, or another qualifying step. The exact process is controlled by the offer provider. Read the current instructions, eligibility rules, reward value, and delivery conditions before participating.'),
        ('Reward values and eligibility', f'Promotions can advertise different reward amounts, including values around ${amount}. A headline should not be treated as a guaranteed payment. Eligibility can depend on location, age, device, campaign availability, completion requirements, and other terms shown with the individual offer.'),
        ('Why people search for gift card rewards', f'Searches for {html.escape(keywords)} often reflect interest in online incentives and shopping-related promotions. A useful approach is to compare the terms of an offer, understand what action is required, and decide only after the requirements are clear.'),
        ('A simple checklist before you start', 'Check the offer terms. Confirm the reward value. Verify regional eligibility. Understand whether one or multiple activities are required. Never share passwords, authentication codes, or unnecessary sensitive information. If the destination feels unclear, stop and review the terms.'),
        ('Explore the current offer destination', 'When you are ready to review current promotional destinations, use the button below. The destination may change its available offers and requirements, so rely on the information displayed there rather than an old headline on this page.'),
    ]
    chosen = sections[:extra]
    faq = f'''<h2>Frequently asked questions</h2><details><summary>Is this an official Amazon page?</summary><p>No. This is an independent promotional information page and is not affiliated with, sponsored by, or endorsed by Amazon.</p></details><details><summary>Is the ${amount} reward guaranteed?</summary><p>No. Reward availability and eligibility depend on the applicable promotion and its current terms.</p></details><details><summary>What should I do before completing an offer?</summary><p>Read the offer requirements, eligibility conditions, reward value and delivery information carefully.</p></details>'''
    body = '\n'.join(f'<section><h2>{h}</h2><p>{p}</p></section>' for h,p in chosen)
    safe_title = html.escape(title)
    kw = html.escape(keywords)
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow,max-image-preview:large"><meta name="description" content="{safe_title}. Explore gift card rewards, promotional offers, qualifying activities, eligibility information and current reward terms."><meta name="keywords" content="{kw}"><meta property="og:title" content="{safe_title}"><meta property="og:description" content="Explore gift card reward information and promotional offers."><title>{safe_title} | Gift Card Rewards</title><style>:root{{--a:{accent};--d:{dark};--ink:#17202a;--muted:#626d7a;--bg:#f5f6f8}}*{{box-sizing:border-box}}body{{margin:0;background:linear-gradient(180deg,#fff,var(--bg));font-family:Arial,Helvetica,sans-serif;color:var(--ink)}}.top{{position:sticky;top:0;z-index:5;background:var(--a);padding:13px;text-align:center;box-shadow:0 4px 18px #0002}}.top a{{color:#111;text-decoration:none;font-weight:900}}.wrap{{max-width:960px;margin:auto;padding:18px}}article{{background:#fff;border:1px solid #e3e6ea;border-radius:22px;padding:clamp(22px,5vw,46px);box-shadow:0 18px 60px #18202a12}}.eyebrow{{display:inline-block;background:#eef1f4;border-radius:999px;padding:7px 11px;font-size:12px;font-weight:800}}h1{{font-size:clamp(38px,8vw,68px);line-height:1.01;letter-spacing:-2px;margin:18px 0}}h2{{font-size:clamp(23px,4vw,31px);margin:38px 0 10px}}p,li{{font-size:17px;line-height:1.78;color:var(--muted)}}.hero{{margin:25px 0;padding:28px;border-radius:20px;background:var(--d);color:#fff}}.hero .price{{font-size:clamp(44px,10vw,72px);font-weight:950;color:var(--a)}}.hero p{{color:#d8dde3}}.cta{{display:inline-block;margin-top:10px;padding:16px 22px;background:var(--a);color:#111;text-decoration:none;border-radius:12px;font-weight:950}}section{{max-width:820px}}details{{padding:17px 0;border-top:1px solid #e5e7eb}}summary{{cursor:pointer;font-weight:800}}footer{{font-size:12px;line-height:1.6;color:#818a96;padding:25px 0 8px}}@media(max-width:600px){{.wrap{{padding:12px}}article{{padding:22px 18px}}p,li{{font-size:16px}}}}
</style></head><body><div class="top"><a href="{TARGET}">→ Explore Your Gift Card Offer</a></div><main class="wrap"><article><span class="eyebrow">Independent Reward Guide · Offer #{idx:02d}</span><h1>{safe_title}</h1><p>Discover practical information about gift card promotions, online rewards and qualifying activities. This page is designed for people comparing reward opportunities and looking for clear terms before they continue.</p><div class="hero"><div class="price">${amount}</div><h2 style="color:#fff;margin-top:8px">Explore available reward opportunities</h2><p>Reward values and requirements vary by promotion. Review the current offer before participating.</p><a class="cta" href="{TARGET}">View Available Offers →</a></div>{body}{faq}<section><h2>Continue to the current offer</h2><p>Use the button below to visit the promotional destination and review the offers currently available to you.</p><a class="cta" href="{TARGET}">Get Started &amp; View Offers →</a></section><footer>Disclosure: This independent page is not affiliated with, sponsored by, or endorsed by Amazon. Amazon and related marks are trademarks of their respective owners. Reward availability, eligibility, values and terms are determined by the applicable offer provider.</footer></article></main></body></html>'''
    (DEST / f'{slug}.html').write_text(page, encoding='utf-8')

print(f'Generated {len(items)} SEO landing pages.')
