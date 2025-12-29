# User Guide

## Getting Started

### Logging In
1. Navigate to `http://localhost:5000`
2. Enter your credentials:
   - Username: `admin`
   - Password: `admin`
3. Click **Login**

### Dashboard Overview
After logging in, you'll see the main dashboard with:
- **Welcome message** showing your username
- **Inventory table** displaying all items
- **Add new item form** at the bottom
- **Logout button** in the top right

## Managing Inventory

### Viewing Items
The dashboard displays all inventory items in a table with columns:
- **ID**: Unique identifier for each item
- **Name**: Item name/description
- **Quantity**: Current stock quantity

### Adding New Items
1. Scroll to the "Add New Item" section
2. Enter the **Item Name**
3. Enter the **Quantity** (numeric value)
4. Click **Add Item**
5. The page will refresh and display the new item

### Data Persistence
- All items are automatically saved to `items.json`
- Data persists between application restarts
- No manual save required

## Session Management

### Staying Logged In
- Your session remains active while the browser is open
- Closing the browser will end your session

### Logging Out
Click the **Logout** button in the top right corner to:
- End your session
- Return to the login page
- Secure your data

## Tips & Best Practices

✅ **Do:**
- Use descriptive item names
- Keep quantities up to date
- Log out when finished

❌ **Don't:**
- Manually edit `items.json` while the app is running
- Share login credentials
- Leave sessions unattended

## Limitations
Current version does not support:
- Editing existing items
- Deleting items
- Multiple user accounts
- Search/filter functionality

These features may be added in future releases.
