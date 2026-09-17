# Free Render workshop deployment

Prepared for 15 participants over two hours. The free Python service was deployed and verified on 17 September 2026.

Live site: https://ai-for-science-workshop.onrender.com
Service: `srv-dalq8om7bikc73a7np9g`, Frankfurt, Free (512 MB, 0.1 CPU).
Verified runtime commit: `94384ca4e63d96e969942b636f47ab19b5ae3f23`. Auto-deploy is off.
The service was configured through the dashboard using these settings.

Use `render.free.yaml` as the Blueprint path, or copy its settings into a Free Python web service. Do not deploy `render.yaml`, which still describes the paid persistent-disk option.

The original `AI_for_science_workshop_v4.zip` is required in the repository root. The existing build script verifies its SHA-256 before extraction. The original archive was retrieved and its expected SHA-256 verified on 17 September 2026.

The free service uses `/tmp/ai-science-workshop`, not a persistent disk. Rooms and uploaded slides are lost when Render restarts, redeploys or spins down the service. Download contributions and the combined deck during the workshop. Participants should retain their original slides. No retention or recovery guarantee is provided by this configuration.

The startup script creates `SCITEST2` with a separately generated management key. Only share `/room/?room=SCITEST2`; keep management keys private. No room exists until the service starts successfully.

Before teaching, verify the public page, upload receipts, gallery, facilitator controls, and editable combined PowerPoint. A 15-submission check and visual inspection of the downloaded deck remain required. Example slides must be clearly identified as examples, not participant submissions.
