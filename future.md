# TrapSight (Clearer-Terms): Architectural Review & Browser AI Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

TrapSight (`clearer-terms`) is a Chrome browser extension (Manifest V3) designed to protect consumers against predatory dark patterns, hidden recurring subscriptions, and deceptive pricing traps during e-commerce checkouts. By intercepting checkout buttons, extracting DOM pricing containers, and querying the Gemini 1.5 Flash API with structured JSON schemas, TrapSight translates confusing legalese into clear arithmetic before payment authorization.

### Architectural Strengths
- **Modular 4-Role Division:** Clear separation between DOM scraping (`scraper.js`), background AI service worker (`background.js`), UI modal injection (`popup.js` / widget styles), and content script orchestration (`content.js`).
- **Structured JSON Contract:** Guarantees strict financial math parsing (`hasHiddenFees`, `basePrice`, `hiddenCharges`, `totalFirstYearCost`) rather than unstructured chatbot advice.
- **Visual Context Highlighting:** Maps AI findings directly back to specific DOM elements via `domSelectorToHighlight` for one-click verification.

### Identified Bottlenecks & Code Smells
1. **Hardcoded CSS Scraper Selectors:** The current scraping logic relies on exact CSS class names for a fixed set of demo sites. Minor layout updates or A/B test variations instantly break extraction.
2. **Privacy & Payment Token Exposure:** Passing full raw text from checkout forms to an external cloud API risks inadvertently transmitting sensitive PII (addresses, phone numbers, partial card digits).
3. **Manifest V3 Worker Termination:** Chrome MV3 background service workers go idle after 30 seconds of inactivity; long-running LLM inferences without keepalive pings risk silent drops.

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: Universal Heuristic Scraper
        P1A[Tree-Walking Semantic DOM Parser] --> P1B[Local PII Masker & Anonymizer]
        P1B --> P1C[MutationObserver Dynamic Checkout Hook]
    end

    subgraph Phase 2: Dark Pattern Classifier & Regulatory Tagging
        P2A[FTC / EU Dark Pattern Taxonomy Engine] --> P2B[Forced Continuity & Roach Motel Detector]
        P2B --> P2C[Hidden Drip-Pricing Arithmetic Verifier]
    end

    subgraph Phase 3: Zero-Latency Local WebAssembly LLM
        P3A[WebLLM / Wasm In-Browser Inference] --> P3B[Quantized SmolLM2 / Qwen 0.5B Model]
        P3B --> P3C[100% Offline Private Contract Auditing]
    end

    subgraph Phase 4: Multi-Browser & Autonomous Cart Protection
        P4A[Firefox WebExtension & Safari Port] --> P4B[Automated One-Click Unsubscribe Assist]
        P4B --> P4C[Community Crowdsourced Dark Pattern Registry]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: Universal Semantic DOM Scraper & Local PII Scrubber
- [ ] **Semantic Tree Extractor:** Implement an autonomous DOM walker that detects cart tables, terms checkboxes, and recurring billing clauses using ARIA roles, microdata tags, and text proximity rather than rigid CSS classes.
- [ ] **Client-Side Regex Sanitizer:** Strip all email addresses, phone numbers, postal codes, and credit card number sequences locally before building the LLM extraction payload.
- [ ] **Single-Page Application (SPA) Support:** Deploy `MutationObserver` hooks to capture dynamically loaded checkout modals (e.g., Stripe Elements, Shopify Buy Buttons).

### Milestone 2: Formal Dark Pattern Classification & Regulatory Mapping
- [ ] **Taxonomy Tagging:** Categorize detected deceptive practices into official regulatory frameworks (FTC Guidelines, EU Digital Services Act):
  - *Hidden Subscriptions / Inertia Selling*
  - *Drip Pricing & Phantom Processing Fees*
  - *Pre-Checked Consent Boxes*
  - *Confirmshaming & Urgency Countdown Clocks*
- [ ] **True Cost Amortization Calculator:** Compute 12-month and 24-month total cost of ownership (TCO) including estimated price hikes after promotional discount expirations.

### Milestone 3: On-Device Private WebAssembly (Wasm) Inference
- [ ] **Local Small Language Model (SLM):** Integrate WebLLM with quantized on-device models (e.g., Qwen 2.5 0.5B / SmolLM2) running directly on WebGPU.
- [ ] **Zero-Data Outbound Guarantee:** Offer an ultra-secure privacy mode where 100% of legal parsing happens in-memory on the user's device with zero external API calls.

### Milestone 4: Cross-Browser Support & Remediation Tools
- [ ] **Firefox & Safari Extension Builds:** Port manifest files and messaging shims for cross-browser web store distribution.
- [ ] **Auto-Cancel Reminders:** Provide a one-click calendar sync (.ics) alert setting reminders 3 days before any trial subscription auto-renews at full price.
