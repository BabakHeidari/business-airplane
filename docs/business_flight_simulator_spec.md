# Business Flight Simulator — Codex Implementation Brief

You are building a production-minded MVP for a gamified business consulting web application called **Business Flight Simulator**.

The goal is to help small-business owners improve their business through a flight-simulator metaphor. The app must feel like a serious strategy game and operating system, not a childish gamified checklist.

Do not use copyrighted or proprietary wording, worksheets, assessments, branding, or course material from Donald Miller or Business Made Simple. The app may use the general six-part airplane metaphor below, but all language, logic, mission templates, UI, questions, and content must be original.

## 1. Product goal

A small-business owner should be able to:

1. Create a business workspace.
2. Complete a business diagnostic across six systems.
3. See a visual “flight status” dashboard.
4. Receive one primary improvement mission at a time.
5. Complete mission tasks and submit evidence.
6. Track weekly KPIs.
7. Receive a weekly flight debrief.
8. View progress over time.
9. Work with a consultant who can review the business, assign missions, add notes, and generate reports.

The product must guide users toward the highest-priority business constraint rather than overwhelm them with dozens of recommendations.

## 2. Six business systems

Use these internal identifiers and original labels:

* `cockpit`: Leadership and focus
* `marketing_engine`: Demand generation and messaging
* `sales_engine`: Sales process and conversion
* `wings`: Product value, pricing, margin, and retention
* `fuselage`: Operations, delivery, quality, and overhead
* `fuel`: Cash flow, runway, and financial resilience

Each system has:

* Score from 0 to 100
* Status: critical, warning, stable, strong
* Short explanation
* Suggested next action
* Relevant KPI set
* Trend versus prior review

Important rule: never let an average score hide a critical issue. For example, if the business has less than 30 days of cash runway, show a highly visible grounded / critical warning even if other systems are strong.

## 3. Target users and roles

Implement role-based access:

* `owner`: creates and manages their business workspace
* `team_member`: can update metrics and complete assigned mission tasks
* `consultant`: can access assigned client businesses, add notes, assign missions, and generate reports
* `admin`: manages all organizations, users, and templates

A user can belong to multiple organizations.

## 4. Core game loop

The app uses a weekly strategy loop:

1. Owner enters or imports a few current business metrics.
2. System evaluates the six business systems.
3. System identifies the largest bottleneck or risk.
4. System assigns one primary mission and optionally one supporting mission.
5. Owner and team complete action steps.
6. They submit evidence or KPI results.
7. System creates a flight debrief with outcomes, next priority, and business trend.

Do not use meaningless gamification such as random coins or cartoon rewards.

Use meaningful game mechanics:

* Flight health
* Critical warnings / turbulence
* Weekly missions
* Mission streaks
* Capability unlocks
* Flight log
* Quarterly campaign
* Verified completion
* Business milestones
* Levels based on operational maturity, not fake XP

Examples of milestones:

* First 13-week cash forecast completed
* First repeatable sales follow-up process installed
* First profitable offer identified
* Four consecutive weekly business reviews completed
* Cash runway improved by 30%
* Conversion rate improved for two consecutive review periods

## 5. MVP scope

Build the following modules.

### A. Authentication and organization setup

Implement:

* Email/password authentication
* Secure password hashing
* Login/logout
* Registration
* Create organization/business workspace
* Invite team members by email placeholder flow
* Select role per member
* Business profile setup

Business profile fields:

* Business name
* Industry
* Business model
* Country/currency
* Team size
* Monthly revenue range
* Monthly fixed-cost range
* Average gross margin range
* Current cash balance
* Primary growth goal
* Main business challenge
* Fiscal year start month

Use Flask-WTF or equivalent CSRF protection for forms.

### B. Diagnostic onboarding

Create a diagnostic with original questions across the six systems.

Requirements:

* Around 5 to 7 questions per system
* Use 1–5 scale answers where appropriate
* Support a mix of multiple choice, numeric inputs, and yes/no questions
* Store responses
* Calculate a score for each system
* Show results immediately after completion
* Allow the diagnostic to be repeated every quarter

Example original question types:

Cockpit:

* Does your business have one written priority for the current quarter?
* Do you hold a recurring decision-making meeting?
* Can the owner explain the business’s main constraint in one sentence?

Marketing Engine:

* Do you know which channel produces the most qualified leads?
* Do you track lead source and lead quality?
* Is your primary offer clearly stated on your website or social media?

Sales Engine:

* Do you record inquiries and their status?
* Do you have a defined follow-up process?
* What is your approximate inquiry-to-sale conversion rate?

Wings:

* Do you know the gross margin of your main products or services?
* Which products create the highest contribution margin?
* Do you track repeat purchases or retention?

Fuselage:

* Do you measure delivery delay, rework, complaints, or operational bottlenecks?
* Is there a documented workflow for your most important customer-facing process?
* Are key recurring tasks dependent on one person?

Fuel:

* Do you know your current cash runway?
* Do you maintain a short-term cash forecast?
* Are receivables, liabilities, and payment dates visible in one place?

Use transparent scoring. Put scoring logic in a service layer, never directly inside templates or route functions.

### C. Flight deck dashboard

Build a visually strong, responsive dashboard with:

* Aircraft / flight status summary
* Overall business health indicator
* Six system cards
* Critical warning banner when needed
* Current primary mission
* Upcoming weekly review date
* Cash runway indicator
* KPI trend chart
* Recent flight log entries
* Mission completion progress
* “What needs attention now?” panel

Do not use a cartoon airplane. Use a clean, modern, premium visual metaphor.

Use status terminology:

* Grounded
* Turbulence
* Stabilizing
* Cruising
* Ready for Growth

Create an original visual system map using cards, gauges, progress bars, and system icons.

### D. Mission engine

Implement a rule-based mission engine first.

Do not make AI required for the initial mission selection.

Mission selection logic:

1. Detect critical thresholds first.
2. Select the lowest-scoring system.
3. Consider business goal and industry.
4. Select a suitable mission template.
5. Avoid assigning the same mission repeatedly.
6. Allow consultant override.
7. Assign one primary mission and at most one supporting mission.

Each mission includes:

* Title
* System
* Why it matters
* Business problem
* Expected impact
* Target KPI
* Baseline KPI
* Target KPI value
* Due date
* Difficulty
* Estimated effort
* Steps
* Evidence requirements
* Completion status
* Notes
* Consultant feedback

Create at least 18 original mission templates, three per system.

Example mission types:

Cockpit:

* Define a single quarterly operating priority
* Run a structured weekly leadership review
* Map top three business constraints

Marketing Engine:

* Clarify the primary offer and customer promise
* Identify top three lead sources
* Run a simple lead-source tracking experiment

Sales Engine:

* Build a follow-up pipeline
* Contact lost leads using a structured script
* Create a simple conversion scorecard

Wings:

* Calculate contribution margin for top products
* Identify and promote the highest-margin offer
* Build a basic repeat-customer offer

Fuselage:

* Map the core customer delivery workflow
* Identify the largest operational delay
* Reduce one recurring operational failure point

Fuel:

* Build a 13-week cash forecast
* Create a weekly cash review
* Identify and reduce a low-value fixed cost

### E. KPI tracking

Create a flexible KPI system.

Required default metrics:

Marketing Engine:

* Qualified leads
* Cost per lead
* Website/social conversion rate
* Lead-source mix

Sales Engine:

* New inquiries
* Conversion rate
* Sales pipeline value
* Average sale value
* Follow-up completion rate

Wings:

* Revenue
* Gross margin
* Contribution margin
* Repeat purchase rate
* Top-product share

Fuselage:

* On-time delivery rate
* Customer issue rate
* Rework rate
* Average fulfillment time
* Fixed-cost ratio

Fuel:

* Cash balance
* Cash runway in days
* Accounts receivable
* Accounts payable
* Weekly operating cash flow

Cockpit:

* Weekly review completion
* Priority completion rate
* Team mission completion rate

Support:

* Manual metric entry
* CSV import for future expansion
* Weekly and monthly frequency
* Historical values
* Trend calculation
* Baseline and target comparisons

### F. Weekly review and flight debrief

Create a weekly review workflow.

The owner should answer:

* What changed this week?
* What improved?
* What got worse?
* What blocked progress?
* What decision was made?
* What is the highest priority next week?

Generate a structured debrief containing:

* Current status
* KPI changes
* Completed missions
* Missed steps
* Main bottleneck
* Recommended next mission
* Key risks
* Consultant notes
* Next review date

Initially generate this using deterministic templates. Add an AI-provider abstraction later, but do not make it necessary for core workflows.

### G. Consultant workspace

Create a consultant dashboard.

Consultants should be able to:

* View assigned client businesses
* Filter businesses by status and risk
* Open client flight deck
* Add private consultant notes
* Assign or override missions
* Review submitted evidence
* See businesses with cash or performance warnings
* Generate a one-page client summary report
* Export a simple PDF-ready HTML report

Do not build a full billing, CRM, or accounting system in this MVP.

## 6. Technical stack

Use:

* Python 3.12+
* Flask
* Jinja templates
* SQLAlchemy
* Flask-Migrate / Alembic
* PostgreSQL for production
* SQLite only for local development and automated tests
* Flask-Login or equivalent secure authentication
* Flask-WTF / CSRF protection
* Bootstrap 5 or clean custom CSS
* HTMX and/or Alpine.js for light interactions
* ECharts or Chart.js for dashboard charts
* Docker Compose
* Pytest
* Ruff or equivalent linting
* `.env.example`
* Clear README setup instructions

Build as a responsive PWA-ready web app:

* Mobile-first responsive layout
* Manifest file
* Basic service worker scaffold
* Installable shell structure
* No native mobile app required

Use a clean, modular architecture:

```text
app/
  __init__.py
  config.py
  extensions.py
  models/
  services/
  blueprints/
  templates/
  static/
  forms/
  utils/
migrations/
tests/
seed/
docker/
```

Use blueprints such as:

```text
auth
organizations
onboarding
dashboard
diagnostics
missions
metrics
reviews
consultant
reports
admin
```

Keep business logic in service classes, not in route handlers.

## 7. Data model

Create database models for:

* User
* Organization
* OrganizationMembership
* BusinessProfile
* SystemDefinition
* DiagnosticQuestion
* DiagnosticAssessment
* DiagnosticResponse
* SystemScore
* MetricDefinition
* MetricEntry
* MissionTemplate
* Mission
* MissionTask
* MissionEvidence
* WeeklyReview
* FlightLogEntry
* ConsultantNote
* Achievement
* OrganizationAchievement
* Alert
* ReportSnapshot

Include created_at and updated_at timestamps where relevant.

Use UUIDs or secure non-sequential public identifiers for externally exposed entities.

## 8. Design requirements

Design style:

* Serious, premium, practical
* Modern strategy-game feeling
* Clean business dashboard
* No childish gamification
* Strong visual hierarchy
* Clear warnings
* Accessible colors and labels
* Mobile responsive
* Card-based layout
* Minimal animation
* Progress should be understandable in less than 10 seconds

Important:

* Never rely only on color to convey status.
* Use accessible labels for critical, warning, stable, and strong states.
* Build templates so localization and RTL can be added later.
* Do not hardcode English copy deep in JavaScript.
* Use reusable components and Jinja partials.

## 9. Security and quality requirements

Implement:

* Password hashing
* CSRF protection
* Role-based access checks
* Organization-level data isolation
* Input validation
* Secure session configuration
* Safe error pages
* Structured logging
* No credentials in source control
* `.env.example`
* Pagination for list pages
* Audit-style flight log for key business actions
* Tests for critical scoring and mission-selection rules

Add tests for:

* System score calculation
* Critical-risk detection
* Cash runway alert logic
* Mission selection
* Role authorization
* Organization data isolation
* Weekly review workflow

## 10. Seed data

Add a demo business called:

“Northstar Coffee”

Industry: café / local food service

Seed:

* Two users: owner and consultant
* Sample diagnostic responses
* Sample system scores
* Ten weeks of KPI history
* At least three completed missions
* One active mission
* One critical or warning alert
* A few consultant notes
* A flight log timeline

The demo should make the app visually usable immediately after setup.

## 11. Delivery process

Work in phases. Do not attempt every module in one change.

Phase 1:

* Project scaffold
* Docker Compose
* Database setup
* Authentication
* Organizations and roles
* Base layout
* Seed demo account
* README

Phase 2:

* Diagnostic onboarding
* Scoring services
* System score storage
* Flight deck dashboard

Phase 3:

* Mission templates
* Rule-based mission selection
* Mission assignment
* Mission tasks and evidence

Phase 4:

* KPI definitions and manual entry
* Charts
* Alerts
* Weekly reviews
* Flight debrief

Phase 5:

* Consultant workspace
* Client overview
* Notes
* Mission override
* Report page

Phase 6:

* PWA shell
* Tests
* Security pass
* UX polish
* Documentation

At the end of each phase:

1. Run tests.
2. Run linting.
3. Explain files changed.
4. Explain migrations created.
5. List manual test steps.
6. Do not rewrite unrelated existing files.
7. Preserve existing base templates and authentication if integrating into an existing Flask project.

Before writing code, inspect the existing repository. If an existing Flask app is present, integrate cleanly instead of replacing the project structure. If no app exists, create the recommended structure.

Begin with Phase 1 only.
