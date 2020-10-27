# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

API_PATH = {
    "config":                  "/api/config/",
    "analyze_domain":          "/api/analyze/domain/",
    "analyze_url":             "/api/analyze/url/",
    "analyze_link":            "/api/analyze/link/",
    "analyze_html":            "/api/analyze/html/",
    "indicators_add":          "/api/indicators/add/",
    "indicators_fetch":        "/api/indicators/fetch/",
    "indicators_fetch_recent": "/api/indicators/fetch/recent/",
    "indicators_fetch_all":    "/api/indicators/fetch/all/",
    "indicators_details":      "/api/indicators/details/{sha256}/",
    "indicators_pending":      "/api/indicators/pending/",
    "indicators_disabled":     "/api/indicators/disabled/",
    "indicators_enable":       "/api/indicators/enable/",
    "indicators_disable":      "/api/indicators/disable/",
    "alerts_add":              "/api/alerts/add/",
    "alerts_fetch":            "/api/alerts/fetch/",
    "reports_add":             "/api/reports/add/",
    "reports_fetch":           "/api/reports/fetch/",
    "reports_details":         "/api/reports/details/{uuid}/",
    "users_pending":           "/api/users/pending/",
    "users_active":            "/api/users/active/",
    "users_activate":          "/api/users/activate/{uuid}/",
    "users_deactivate":        "/api/users/deactivate/{uuid}/",
}
