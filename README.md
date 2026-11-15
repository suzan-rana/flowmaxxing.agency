# flowmaxxing.agency

Marketing site for Flowmaxxing — Meta and TikTok paid social.

One page plus a stylesheet, no build step and no dependencies:

| File | What it is |
|---|---|
| `index.html` | The whole site: hero, services, playbooks, the wall, process, the weekly loop, testimonials, FAQ, contact |
| `styles.css` | Stylesheet |
| `media/` | Your ad stills and client photos go here |

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8899
```

## Filling the wall

Seven cards, Pinterest-style masonry. To fill one, replace its `<span class="ps">` with:

```html
<img src="media/your-ad.jpg" alt="">
```

and swap `[ client ]` in the caption for the brand name. The client name is the part doing the persuading — a card without one is decoration.

Ratios are 9:16, 4:5, 1:1 and 16:9, matching what actually runs on Meta and TikTok. Cards sit at slight angles and straighten on hover.

## Deploy

Works as-is on any static host with the repo root as the publish directory.

- **GitHub Pages** — Settings → Pages → deploy from `main` / root. `CNAME` already points at the apex domain; add the DNS records GitHub gives you.
- **Cloudflare Pages / Vercel / Netlify** — connect the repo, no build command, output directory `/`.

## Sample content — must be replaced

Chapter 06 is filled with **invented** names, companies and quotes so the board can be judged full. Nobody said these words and none of them are clients. The section carries a visible sample flag saying so.

Publishing invented customer reviews as genuine is misleading conduct in most markets, and it is trivially caught. Before launch, either replace every card with a quote the person has signed off in writing, or delete the chapter. Then delete the `.sample-flag` paragraph.

## Before it goes public

The page carries visible dashed slots for everything that needs real input. Search the file for `class="slot"` and fill or delete each one.

- Base location (hero, top right)
- Ad videos and stills for the work grid, plus a client name on each card
- Replace the nine sample testimonials (Chapter 06) and remove the sample flag — each real quote needs written sign-off, each photo needs a licence
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
