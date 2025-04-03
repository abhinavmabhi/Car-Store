from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        value = float(value)
        if value >= 1_00_00_000:  # 1 crore
            return f"{value / 1_00_00_000:.2f} Cr"
        elif value >= 1_00_000:  # 1 lakh
            return f"{value / 1_00_000:.2f} Lakh"
        else:
            return f"{value:,.0f}"  # Normal formatting with commas
    except (ValueError, TypeError):
        return value  # Return as-is if conversion fails
    

