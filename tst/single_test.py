import unittest
from organization import Organization

class TestOrganizationSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        org1 = Organization(code='001', name='Company A', address='123 Main St', postal_code='12345')
        org2 = Organization()

        self.assertIs(org1, org2)

    def test_initial_properties(self):
        org = Organization(code='001', name='Company A', address='123 Main St', postal_code='12345')

        self.assertEqual(org.code, '001')
        self.assertEqual(org.name, 'Company A')
        self.assertEqual(org.address, '123 Main St')
        self.assertEqual(org.postal_code, '12345')

    def test_update_properties(self):
        org = Organization(code='001', name='Company A', address='123 Main St', postal_code='12345')
        org.update(name='Company B', address='456 Another St')
        org.postal_code = "54321"

        self.assertEqual(org.name, 'Company B')
        self.assertEqual(org.address, '456 Another St')
        self.assertEqual(org.postal_code, "54321")

    def test_no_reinitialization(self):
        org1 = Organization(code='001', name='Company A', address='123 Main St', postal_code='12345')
        org2 = Organization()

        self.assertEqual(org2.code, '001')
        self.assertEqual(org2.name, 'Company A')
        self.assertEqual(org2.address, '123 Main St')
        self.assertEqual(org2.postal_code, '12345')

if __name__ == '__main__':
    unittest.main()
