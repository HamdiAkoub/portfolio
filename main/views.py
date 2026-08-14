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
                "tagline": "Selected snippets from the project, built for a "
                           "local LAN deployment, privately hosted.",
                "stack": [
                    "Django 5",
                    "MS SQL Server",
                    "Waitress (WSGI)",
                    "WhiteNoise",
                    "Tailwind + Alpine.js",
                    "PyArmor + PyInstaller",
                    "IDE Pycharm",
                ],
            },
            "images": [
                {"src": f"img_WM/{name}", "caption": name.rsplit(".", 1)[0]}
                for name in images
            ],
        },
    )

def rest_mgr(request):
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
                "tagline": "Selected snippets from the project, built for a "
                           "local LAN deployment, privately hosted.",
                "stack": [
                    "Django 5",
                    "MS SQL Server",
                    "Waitress (WSGI)",
                    "WhiteNoise",
                    "Tailwind + Alpine.js",
                    "PyArmor + PyInstaller",
                    "IDE Pycharm",
                ],
            },
            "images": [
                {"src": f"img_WM/{name}", "caption": name.rsplit(".", 1)[0]}
                for name in images
            ],
        },
    )
