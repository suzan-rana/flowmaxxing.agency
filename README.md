# flowmaxxing.agency

Marketing site for Flowmaxxing — Meta and TikTok paid social.

Three static files, no build step and no dependencies:

| File | What it is |
|---|---|
| `index.html` | Homepage. Hero, services, playbooks, work teaser, process, the weekly loop, testimonials, FAQ, contact |
| `work.html` | The work grid — every ad, four columns, filterable by platform |
| `styles.css` | Shared stylesheet for both pages |
| `media/` | Your ad videos and stills go here |

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8899
```

## Filling the work grid

Each card holds a placeholder. To fill one, replace its `<span class="ps">` with:

```html
<video src="media/your-ad.mp4" poster="media/your-ad.jpg" autoplay muted loop playsinline></video>
```

and swap `[ client ]` in `.logo-badge` for the brand name. The logo badge is the part doing the persuading — a card without one proves nothing.

Ratios are 9:16 for video and 4:5 for statics, matching what actually runs on Meta and TikTok.

## Deploy

Works as-is on any static host with the repo root as the publish directory.

- **GitHub Pages** — Settings → Pages → deploy from `main` / root. `CNAME` already points at the apex domain; add the DNS records GitHub gives you.
- **Cloudflare Pages / Vercel / Netlify** — connect the repo, no build command, output directory `/`.

## Before it goes public

The page carries visible dashed slots for everything that needs real input. Search the file for `class="slot"` and fill or delete each one.

- Base location (hero, top right)
- Ad videos and stills for the work grid, plus a client name on each card
- Client photos and quotes for the testimonial board (Chapter 06) — each needs a licence and written sign-off
- Minimum monthly spend and onboarding timeline (FAQ Q3, Q6)
- Booking calendar URL (Connect)
- Social links, privacy and terms (footer)

Check `hello@flowmaxxing.agency` is the address you want — it appears in the contact row, the mailto link, the copy button and the form draft.

## The contact form

A static page has nowhere to post, so the form composes the enquiry and offers Copy / Open in mail app. It never claims to have sent anything. To make it real, point `#reviewForm` at a handler (Formspree, a Cloudflare Worker, or your own endpoint).

## Design

- Paper `#F9F4EC`, pure black chapters, one cobalt accent `#1F3AFF`
- Instrument Sans at 600 throughout, DM Mono for micro-labels
- Tokens are the `:root` block at the top of the `<style>`; change colours and faces there
