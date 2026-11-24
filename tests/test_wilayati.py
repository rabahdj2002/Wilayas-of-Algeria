import pytest

from wilayati import handler


@pytest.fixture()
def h():
    return handler()


class TestSearchByCode:
    def test_valid_code(self, h):
        wilaya = h.searchByCode(16)
        assert wilaya["name"] == "Alger"
        assert wilaya["ar_name"] == "الجزائر"

    def test_first_and_last(self, h):
        assert h.searchByCode(1)["name"] == "Adrar"
        assert h.searchByCode(58)["id"] == "58"

    def test_string_code(self, h):
        assert h.searchByCode("16")["name"] == "Alger"

    @pytest.mark.parametrize("bad", [0, -1, 59, 100])
    def test_out_of_range(self, h, bad):
        with pytest.raises(ValueError):
            h.searchByCode(bad)

    @pytest.mark.parametrize("bad", [None, "abc", 16.7, [16], True])
    def test_invalid_type(self, h, bad):
        with pytest.raises(ValueError):
            h.searchByCode(bad)


class TestSearchByName:
    def test_exact_name(self, h):
        assert h.searchByName("Alger")["id"] == "16"

    def test_case_insensitive(self, h):
        assert h.searchByName("alger")["id"] == "16"
        assert h.searchByName("CONSTANTINE")["name"] == "Constantine"

    def test_not_found(self, h):
        with pytest.raises(ValueError):
            h.searchByName("NotAWilaya")

    @pytest.mark.parametrize("bad", [None, "", "   ", 16, ["Alger"]])
    def test_invalid_name(self, h, bad):
        with pytest.raises(ValueError):
            h.searchByName(bad)


class TestGetBaladiyat:
    def test_returns_list(self, h):
        baladiyat = h.getBaladiyat(16)
        assert isinstance(baladiyat, list)
        assert len(baladiyat) > 0

    def test_all_belong_to_wilaya(self, h):
        for b in h.getBaladiyat(25):
            assert b["wilaya_id"] == "25"

    def test_constantine_count(self, h):
        # Constantine has 12 communes
        assert len(h.getBaladiyat(25)) == 12

    @pytest.mark.parametrize("bad", [0, 59, None, "x"])
    def test_invalid_code(self, h, bad):
        with pytest.raises(ValueError):
            h.getBaladiyat(bad)


class TestSearchBaladiya:
    def test_exact_name(self, h):
        result = h.searchBaladiya("Ouled Fayet")
        assert result["name"] == "Ouled Fayet"
        assert result["wilaya_id"] == "16"

    def test_partial_match(self, h):
        assert "Constantine" in h.searchBaladiya("Constant")["name"]

    def test_case_insensitive(self, h):
        assert h.searchBaladiya("ouled fayet")["name"] == "Ouled Fayet"

    def test_not_found(self, h):
        with pytest.raises(ValueError):
            h.searchBaladiya("NoSuchBaladiya123")

    @pytest.mark.parametrize("bad", [None, "", 16])
    def test_invalid_name(self, h, bad):
        with pytest.raises(ValueError):
            h.searchBaladiya(bad)


class TestDataIntegrity:
    def test_58_wilayas(self, h):
        codes = {w["id"] for w in (h.searchByCode(c) for c in range(1, 59))}
        assert len(codes) == 58

    def test_commune_count(self, h):
        total = sum(len(h.getBaladiyat(c)) for c in range(1, 59))
        assert total == 1541
