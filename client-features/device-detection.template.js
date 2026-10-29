/**
 * ==============================================================================
 * UNIVERSAL DEVICE & OS DETECTION TEMPLATE
 * ==============================================================================
 * Zero-dependency, lightweight (~1 KB) client-side operating system detector.
 * Automatically identifies:
 *  - Android (Phones & Tablets)
 *  - Apple iOS (iPhone & iPad, including iPadOS desktop mode)
 *  - Apple macOS (MacBook, iMac, Mac Mini)
 *  - Windows PC (Windows 10 / 11)
 *  - Linux
 *
 * Usage:
 * Call `detectDevice()` on DOMContentLoaded to update UI download buttons,
 * platform badges, and card highlights.
 * ==============================================================================
 */

(function() {
  const RELEASE_BASE_URL = "https://github.com/:owner/:repo/releases/download/v2.0.0";

  function detectOS() {
    const ua = navigator.userAgent || navigator.vendor || window.opera || "";
    const platform = navigator.platform || "";

    // 1. Android Detection
    if (/android/i.test(ua)) {
      return "android";
    }

    // 2. iOS (iPhone, iPod, iPad) & iPadOS (where Safari requests desktop Mac site)
    const isIPadOS = platform === "MacIntel" && navigator.maxTouchPoints > 1;
    if (/iPad|iPhone|iPod/.test(ua) || isIPadOS) {
      return "ios";
    }

    // 3. Apple macOS
    if (/Macintosh|Mac OS X/i.test(ua) || /MacIntel/i.test(platform)) {
      return "macos";
    }

    // 4. Windows PC
    if (/Win32|Win64|Windows/i.test(ua) || /Win/i.test(platform)) {
      return "windows";
    }

    // 5. Linux
    if (/Linux/i.test(ua) || /Linux/i.test(platform)) {
      return "linux";
    }

    return "unknown";
  }

  function applyDeviceUI() {
    const os = detectOS();
    const badge = document.getElementById("deviceBadge");
    const heroBtn = document.getElementById("primaryDownloadBtn");
    const metaNote = document.getElementById("fileMetaNote");

    // Remove active highlights from all platform cards
    document.querySelectorAll(".platform-card").forEach(c => c.classList.remove("highlighted"));

    switch(os) {
      case "android":
        if (badge) badge.innerHTML = "<span>📱 Detected: Android Device</span>";
        if (heroBtn) {
          heroBtn.href = `${RELEASE_BASE_URL}/App-Android.apk`;
          heroBtn.innerHTML = "<span>📥 Download for Android (.apk)</span>";
        }
        if (metaNote) metaNote.innerText = "Direct APK Package • ~8 MB";
        highlightCard("card-android");
        break;

      case "ios":
        if (badge) badge.innerHTML = "<span>🍏 Detected: Apple iOS (iPhone / iPad)</span>";
        if (heroBtn) {
          heroBtn.href = `${RELEASE_BASE_URL}/App-iOS.zip`;
          heroBtn.innerHTML = "<span>📥 Download for iOS (SwiftUI)</span>";
        }
        if (metaNote) metaNote.innerText = "Native iOS Package • Install via AltStore/TestFlight";
        highlightCard("card-ios");
        break;

      case "macos":
        if (badge) badge.innerHTML = "<span>🍏 Detected: Apple Mac (macOS)</span>";
        if (heroBtn) {
          heroBtn.href = `${RELEASE_BASE_URL}/App-macOS.dmg`;
          heroBtn.innerHTML = "<span>📥 Download for macOS (.dmg)</span>";
        }
        if (metaNote) metaNote.innerText = "Drag-and-Drop DMG Installer • Apple Silicon & Intel";
        highlightCard("card-macos");
        break;

      case "windows":
      default:
        if (badge) badge.innerHTML = "<span>💻 Detected: Windows PC</span>";
        if (heroBtn) {
          heroBtn.href = `${RELEASE_BASE_URL}/App-Setup.exe`;
          heroBtn.innerHTML = "<span>📥 Download for Windows (.exe)</span>";
        }
        if (metaNote) metaNote.innerText = "Installer Wizard inside .zip • x64 • ~70 MB";
        highlightCard("card-windows");
        break;
    }
  }

  function highlightCard(cardId) {
    const card = document.getElementById(cardId);
    if (card) {
      card.classList.add("highlighted");
    }
  }

  // Auto-run when DOM is interactive
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyDeviceUI);
  } else {
    applyDeviceUI();
  }

  // Export for testing / manual triggering
  window.detectOS = detectOS;
  window.applyDeviceUI = applyDeviceUI;
})();
