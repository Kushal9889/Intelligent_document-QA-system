print("=== Testing Python Execution ===")
print("If you see this, Python is working!")

# Test imports one by one
print("\nTesting imports...")

try:
    import requests
    print("✓ requests imported")
except Exception as e:
    print(f"✗ requests failed: {e}")

try:
    from langchain_community.document_loaders import TextLoader
    print("✓ langchain_community imported")
except Exception as e:
    print(f"✗ langchain_community failed: {e}")

print("\n=== Test Complete ===")
