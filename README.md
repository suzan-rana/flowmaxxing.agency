# flowmaxxing.agency

Marketing site for Flowmaxxing — Meta and TikTok paid social.

One static HTML file. No build step, no dependencies. Open `index.html` in a browser to work on it.

## Deploy

Works as-is on any static host with the repo root as the publish directory.

- **GitHub Pages** — Settings → Pages → deploy from `main` / root. `CNAME` already points at the apex domain; add the DNS records GitHub gives you.
- **Cloudflare Pages / Vercel / Netlify** — connect the repo, no build command, output directory `/`.

## Before it goes public

The page carries visible dashed slots for everything that needs real input. Search the file for `class="slot"` and fill or delete each one.

- Base location (hero, top right)
- Three case studies (Chapter 03)
- Prices for all three tiers (Chapter 08)
- Minimum monthly spend and onboarding timeline (FAQ Q3, Q6)
- Three free-tool links (end of Chapter 09)
- Booking calendar URL (Connect)
- Social links, privacy and terms (footer)
- Advertising-compliance and data-handling line (end of Chapter 06)

Check `hello@flowmaxxing.agency` is the address you want — it appears in the contact row, the mailto link, the copy button and the form draft.

## The contact form

A static page has nowhere to post, so the form composes the enquiry and offers Copy / Open in mail app. It never claims to have sent anything. To make it real, point `#reviewForm` at a handler (Formspree, a Cloudflare Worker, or your own endpoint).

## Design

- Paper `#F9F4EC`, pure black chapters, one cobalt accent `#1F3AFF`
- Instrument Sans at 600 throughout, DM Mono for micro-labels
- Tokens are the `:root` block at the top of the `<style>`; change colours and faces there
