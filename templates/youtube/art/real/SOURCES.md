# Real pictures

Sean, 2026-10-29: "in my slides, there to be real pictures, real screenshots" / "you can get real pics from online
even if they are placeholders". Two kinds live here, and the file name says which:

- **Ours (real, keep):** cut from the After Harvest VSL in Figma (file `EoJfQnkEBeslSHoDOzSSBm`, page node `1:51`,
  downloaded with the Figma connector's `download_assets`). These are our own proof and our own event.
- **`stock-*` (placeholders):** free photos from picjumbo.com (free licence, no credit needed). Swap each for a real
  photo or screenshot of ours when we have one.

| file | what it is | where it came from | used on |
|---|---|---|---|
| launch-lab-registration-page.jpg | Launch Lab's registration page ("Lock In Your Spot", QR code), a 3-day live event, June 9-11 | Figma VSL raw image r09 (2940x1722), downsized | s3 |
| launch-lab-ticket.png | the Launch Lab ticket (June 9-11, 3PM EST, Live Zoom, free seat) | cut from r09, crop (48,468,292,580) of the 1400 px copy | s3, s8 |
| jay-clouse-lab-page.jpg | Jay Clouse's The Lab page | Figma VSL raw image r03 (2380x1566) | not yet |
| jay-the-lab-group.jpg | The Lab members' group photo, from Jay's page | cut from r03, crop (958,490,1284,666) of the 1400 px copy | s7 |
| jay-unreal-collective-zoom.jpg | a live Zoom session, from Jay's page | cut from r03, crop (124,490,448,666) of the 1400 px copy | s8 |
| jay-post-and-chat.png | Jay's "$100,000+ launch" post on X (9:45 PM, 7/9/26) beside our chat with him (3:57 AM, 8:47 AM) | `../figma/proof-jay-clouse-tweet-and-chat.png` (480x270, the only size in the file), 2x Lanczos + unsharp | spare |
| jay-post.png, jay-chat.png | the same, split into the post and the chat. The chat's "right nov" is cut in the original screenshot | from jay-post-and-chat.png | s7 |
| stock-calendar-thursday-31.jpg | calendar app icon, Thursday 31 | https://picjumbo.com/calendar-app-icon-for-time-management/ | s10 |
| stock-whiteboard-teaching.jpg | someone writing a list on a whiteboard | https://picjumbo.com/team-leader-writing-on-white-board/ | s10 |
| stock-buying-on-laptop.jpg | someone paying by card on a laptop | https://picjumbo.com/woman-purchasing-a-product-with-credit-card/ | s10 |
| stock-mail-24-unread.jpg | Mail icon with 24 unread | https://picjumbo.com/notifications-in-email-messages-apps-zero-inbox/ | s8 |
| stock-phone-sales.jpg | a sales dashboard on a phone | https://picjumbo.com/gumroad-dashboard-app-online-selling-digital-goods/ | not yet |
| stock-paper-week-planner.jpg | a paper week planner | https://picjumbo.com/creative-woman-planning-her-week-in-calendar-feminine-style/ | not yet |

Where the rest of the web was closed from a cloud session (2026-10-29): Unsplash (bot check), Pexels, Pixabay,
StockSnap, rawpixel and Freepik (403), Openverse (unreachable), Wikimedia (429). picjumbo works with `curl`.
