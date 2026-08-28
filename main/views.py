from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def warehouse_manager(request):
    # Filenames in display order. Caption = filename without extension.
    images = [
        "Branch_recurr_qry.png",
        "Clients_recurr_qry.png",
        "Balance_qry.png",
        "Cheques_balance.png",
        "Order_stages.png",
        "currency_helper.png",
        "number_sequence_helper.png",
    ]
    return render(
        request,
        "main/warehouse_manager.html",
        {
            "project": {
              "title": "Warehouse Manager",
              "tagline": "Selected snippets from the project, built for "
                         "local server hosting, publically accessed through subdomains tunneling.",
                "stack": [
                  "Django 5",
                  "MS SQL Server",
                  "Integrated into legacy database",
                  "Waitress (WSGI)",
                  "WhiteNoise",
                  "Tailwind + Alpine.js",
                  "PyArmor + PyInstaller",
                  "IDE VS Code",
                ],
            },
            "images": [
              {"src": f"img_WM/{name}", "caption": name.rsplit(".", 1)[0]}
              for name in images
            ],
        },
    )

def rest_mgr(request):
    images = [
        "New_order_detection.png",
        "Guide_normalization.png",
        "Drivers_report_CTE.png",
        "Cash_close_incremental.png",
        "Audit_reconcile.png",
    ]
    return render(
        request,
        "main/RestMgr.html",
        {
            "project": {
                "title": "Restaurant Manager",
                "tagline": "Selected snippets from the project, built for a "
                           "local LAN deployment and API requests from outside the network, privately hosted."
                           "The project mainly handles receiving live orders on the spot through API requests,"
                           " where it manages the distribution of these orders between the current active "
                           "drivers if the order is for delivery, and the handing over to customers if it's a pickup."
                           "In addition, it keeps and stores records of all orders' drivers, stages, amounts...etc. "
                           "This data is also used to provide the ability to close the shift of the current employee,"
                           "and printing detailed summary of that shift.",
                "stack": [
                    "Django",
                    "SQL Server",
                    "React",
                    "Integrated into legacy database",
                    "WhiteNoise",
                    "IDE Pycharm",
                ],
            },
            "images": [
                {"src": f"img_OM/{name}", "caption": name.rsplit(".", 1)[0]}
                for name in images
            ],
        },
    )
